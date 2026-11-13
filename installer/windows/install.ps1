param(
    [Parameter(Mandatory = $true)][string]$BaseDirectory,
    [Parameter(Mandatory = $true)][string]$StatusFile,
    [string]$GamePath,
    [string]$SteamRootOverride,
    [string]$StateRootOverride,
    [switch]$Launch
)

$ErrorActionPreference = 'Stop'
$ExpectedAppId = '2009010'
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Status([string]$Kind, [string]$Message) {
    [System.IO.File]::WriteAllText($StatusFile, "$Kind`n$Message", $Utf8NoBom)
}

function Get-Sha256([string]$Path) {
    if (-not [IO.File]::Exists($Path)) { return $null }
    $stream = [IO.File]::OpenRead($Path)
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($sha.ComputeHash($stream)).Replace('-', '').ToLowerInvariant() }
    finally { $sha.Dispose(); $stream.Dispose() }
}

function Get-VdfValue([string]$Text, [string]$Name) {
    $match = [regex]::Match($Text, '"' + [regex]::Escape($Name) + '"\s+"([^"]*)"', 'IgnoreCase')
    if (-not $match.Success) { return $null }
    return $match.Groups[1].Value
}

function Get-SafePath([string]$Root, [string]$Relative) {
    if ($Relative -notmatch '^[A-Za-z0-9_.+ -]+(/[A-Za-z0-9_.+ -]+)*$') {
        throw "Unsafe path in the localization package: $Relative"
    }
    $path = $Root
    foreach ($part in $Relative.Split('/')) {
        if ($part -eq '.' -or $part -eq '..' -or $part.EndsWith('.') -or $part.EndsWith(' ')) {
            throw "Unsafe path in the localization package: $Relative"
        }
        $path = [IO.Path]::Combine($path, $part)
        Assert-PlainPath $path
    }
    return $path
}

function Assert-PlainPath([string]$Path) {
    try {
        $attributes = [IO.File]::GetAttributes($Path)
    } catch [IO.FileNotFoundException], [IO.DirectoryNotFoundException] {
        return
    }
    if ($attributes -band [IO.FileAttributes]::ReparsePoint) {
        throw "The installer cannot use a linked file or folder: $Path"
    }
}

function Assert-PackagePath([string]$Path) {
    if ($Path -notmatch '^(\.vnrevival-protogen/runtime/.+|game/(fonts/vnrevival/[^/]+|vnrevival_protogen_(display|fonts|preferences)\.rpyc?|tl/[a-z_]+/vnrevival_protogen_(rendering|text)\.rpyc?))$') {
        throw "Unexpected localization path: $Path"
    }
}

function Get-InstallationStateRoot($Installation, [string]$Override) {
    if (-not [string]::IsNullOrWhiteSpace($Override)) {
        return [System.IO.Path]::GetFullPath($Override)
    }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($Installation.GameRoot.ToLowerInvariant())
        $hash = $sha.ComputeHash($bytes)
    } finally {
        $sha.Dispose()
    }
    $installationId = -join ($hash[0..7] | ForEach-Object { $_.ToString('x2') })
    $localData = [Environment]::GetFolderPath([Environment+SpecialFolder]::LocalApplicationData)
    if ([string]::IsNullOrWhiteSpace($localData)) { throw 'The local application data folder was not found.' }
    return Join-Path (Join-Path $localData 'VNR/2009010') $installationId
}

function Resolve-GameRoot([string]$InstallRoot) {
    $exe = Join-Path $InstallRoot 'MyFurryProtogen.exe'
    $data = Join-Path $InstallRoot 'game'
    if ((Test-Path -LiteralPath $exe -PathType Leaf) -and (Test-Path -LiteralPath $data -PathType Container)) {
        Assert-PlainPath $InstallRoot
        return [pscustomobject]@{ GameRoot = $InstallRoot; DataRoot = $InstallRoot; Executable = $exe }
    }
    return $null
}

function Get-SteamRoots([string]$Override) {
    $roots = New-Object System.Collections.Generic.List[string]
    if (-not [string]::IsNullOrWhiteSpace($Override)) {
        $roots.Add(([System.IO.Path]::GetFullPath($Override)))
    }
    foreach ($entry in @(
        @{ Path = 'HKCU:\Software\Valve\Steam'; Name = 'SteamPath' },
        @{ Path = 'HKLM:\SOFTWARE\WOW6432Node\Valve\Steam'; Name = 'InstallPath' },
        @{ Path = 'HKLM:\SOFTWARE\Valve\Steam'; Name = 'InstallPath' }
    )) {
        try {
            $value = (Get-ItemProperty -LiteralPath $entry.Path -Name $entry.Name -ErrorAction Stop).($entry.Name)
            if ($value) { $roots.Add(([System.IO.Path]::GetFullPath($value.Replace('/', '\')))) }
        } catch { }
    }
    foreach ($programFiles in @(${env:ProgramFiles(x86)}, $env:ProgramFiles)) {
        if ($programFiles) { $roots.Add((Join-Path $programFiles 'Steam')) }
    }
    foreach ($root in $roots.ToArray()) {
        $libraries = Join-Path $root 'steamapps/libraryfolders.vdf'
        if (-not (Test-Path -LiteralPath $libraries -PathType Leaf)) { continue }
        $text = [System.IO.File]::ReadAllText($libraries)
        foreach ($match in [regex]::Matches($text, '"path"\s+"([^"]+)"', 'IgnoreCase')) {
            $roots.Add(([System.IO.Path]::GetFullPath($match.Groups[1].Value.Replace('\\', '\'))))
        }
    }
    return @($roots | Select-Object -Unique)
}

function Find-GameInstallation([string]$SelectedPath) {
    $roots = @(Get-SteamRoots $SteamRootOverride)
    if ($SelectedPath) {
        $selected = [IO.Path]::GetFullPath($SelectedPath).TrimEnd([IO.Path]::DirectorySeparatorChar)
        $common = Split-Path -Parent $selected
        if ((Split-Path -Leaf $common) -eq 'common') {
            $apps = Split-Path -Parent $common
            if ((Split-Path -Leaf $apps) -eq 'steamapps') { $roots += Split-Path -Parent $apps }
        }
    }
    foreach ($steamRoot in $roots) {
        $manifestPath = Join-Path $steamRoot "steamapps/appmanifest_$ExpectedAppId.acf"
        if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) { continue }
        $manifestText = [IO.File]::ReadAllText($manifestPath)
        $appId = Get-VdfValue $manifestText 'appid'
        $installDir = Get-VdfValue $manifestText 'installdir'
        $buildId = Get-VdfValue $manifestText 'buildid'
        if ($appId -ne $ExpectedAppId -or $installDir -ne 'My Furry Protogen' -or $buildId -notmatch '^\d+$') { continue }
        $installRoot = Join-Path $steamRoot "steamapps/common/$installDir"
        if ($SelectedPath -and -not $installRoot.Equals($selected, [StringComparison]::OrdinalIgnoreCase)) { continue }
        $resolved = Resolve-GameRoot $installRoot
        if ($null -eq $resolved) { continue }
        $resolved | Add-Member -NotePropertyName BuildId -NotePropertyValue $buildId
        return $resolved
    }
    if ($SelectedPath) { throw 'Choose the My Furry Protogen folder registered in your Steam library.' }
    throw 'My Furry Protogen was not found. Choose its Steam game folder.'
}

function Write-JsonFile($Value, [string]$Path) {
    $parent = Split-Path -Parent $Path
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    $temporary = "$Path.new"
    Assert-PlainPath $temporary
    [IO.File]::WriteAllText($temporary, (($Value | ConvertTo-Json -Depth 12) + "`n"), $Utf8NoBom)
    if ([IO.File]::Exists($Path)) {
        $previous = "$Path.previous"
        Assert-PlainPath $previous
        [IO.File]::Replace($temporary, $Path, $previous)
        [IO.File]::Delete($previous)
    } else {
        [IO.File]::Move($temporary, $Path)
    }
}

function Read-Receipt([string]$Path, [string]$PackageId) {
    Assert-PlainPath $Path
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $null }
    $receipt = [System.IO.File]::ReadAllText($Path) | ConvertFrom-Json
    if ([int]$receipt.schemaVersion -ne 1 -or [string]$receipt.packageID -ne $PackageId) {
        throw 'The previous VN Revival installation data could not be verified.'
    }
    return $receipt
}

function Recover-Transaction([string]$StateRoot, [string]$DataRoot, [string]$ReceiptPath) {
    $transaction = Join-Path $StateRoot 'transaction'
    Assert-PlainPath $transaction
    if (-not (Test-Path -LiteralPath $transaction -PathType Container)) { return }
    $statePath = Join-Path $transaction 'state.json'
    Assert-PlainPath $statePath
    if (-not (Test-Path -LiteralPath $statePath -PathType Leaf)) {
        Remove-Item -LiteralPath $transaction -Recurse -Force
        return
    }
    $state = [System.IO.File]::ReadAllText($statePath) | ConvertFrom-Json
    if ([int]$state.schemaVersion -ne 1 -or $state.packageID -ne 'fun.vnrevival.protogen') {
        throw 'The interrupted installation record is malformed.'
    }
    if (-not [bool]$state.committed) {
        $rollbackRoot = Join-Path $transaction 'rollback'
        Assert-PlainPath $rollbackRoot
        $previousReceipt = Join-Path $transaction 'previous-receipt.json'
        Assert-PlainPath $previousReceipt
        if ($state.previousReceiptSHA256 -and (Get-Sha256 $previousReceipt) -ne $state.previousReceiptSHA256) {
            throw 'The interrupted installation is missing its verified previous receipt.'
        }
        # Check the entire rollback before restoring any member. A retry can resume from
        # either the before or after state. Refuse to overwrite subsequent foreign edits.
        $restore = @(foreach ($file in $state.files) {
            Assert-PackagePath ([string]$file.path)
            $destination = Get-SafePath $DataRoot ([string]$file.path)
            $current = Get-Sha256 $destination
            if ($current -eq $file.beforeSHA256) { continue }
            if ($current -ne $file.afterSHA256) { throw "A file changed after interruption: $($file.path)" }
            $backup = Get-SafePath $rollbackRoot ([string]$file.path)
            if ($file.beforeSHA256 -and (Get-Sha256 $backup) -ne $file.beforeSHA256) {
                throw "The rollback copy could not be verified: $($file.path)"
            }
            @{ destination = $destination; backup = $backup; sha256 = $file.beforeSHA256 }
        })
        foreach ($item in $restore) {
            if ($item.sha256) { Copy-Item -LiteralPath $item.backup -Destination $item.destination -Force }
            else { Remove-Item -LiteralPath $item.destination -Force }
            if ((Get-Sha256 $item.destination) -ne $item.sha256) {
                throw "Could not restore $($item.destination)"
            }
        }
        if ($state.previousReceiptSHA256) {
            Copy-Item -LiteralPath $previousReceipt -Destination $ReceiptPath -Force
        } elseif (Test-Path -LiteralPath $ReceiptPath -PathType Leaf) {
            Remove-Item -LiteralPath $ReceiptPath -Force
        }
    }
    Remove-Item -LiteralPath $transaction -Recurse -Force
}

function Get-Edition($Config, $Installation) {
    if ($Installation.BuildId -ne [string]$Config.steamBuildID) {
        throw "Steam build $($Installation.BuildId) is unsupported by this installer."
    }
    $matches = @(foreach ($edition in $Config.editions) {
        $match = $true
        foreach ($source in $edition.original.PSObject.Properties) {
            if ((Get-Sha256 (Get-SafePath $Installation.GameRoot $source.Name)) -ne $source.Value) {
                $match = $false
                break
            }
        }
        if ($match) { $edition }
    })
    if ($matches.Count -ne 1) { throw 'The Steam game files did not match a supported base game or DLC.' }
    return $matches[0]
}

function Get-OwnedFiles($Receipt) {
    $files = @{}
    if ($null -eq $Receipt) { return $files }
    foreach ($file in $Receipt.files) {
        Assert-PackagePath ([string]$file.path)
        if ($files.ContainsKey([string]$file.path) -or $file.installedSHA256 -notmatch '^[a-f0-9]{64}$') {
            throw 'The previous VN Revival installation data could not be verified.'
        }
        $files.Add([string]$file.path, [string]$file.installedSHA256)
    }
    return $files
}

function Test-CompiledScript([string]$Bytecode, [string]$Source) {
    $bytes = [IO.File]::ReadAllBytes($Bytecode)
    if ($bytes.Length -lt 26 -or [Text.Encoding]::ASCII.GetString($bytes, 0, 10) -cne 'RENPY RPC2') { return $false }
    $embedded = [BitConverter]::ToString($bytes, $bytes.Length - 16, 16).Replace('-', '')
    return (Get-FileHash -LiteralPath $Source -Algorithm MD5).Hash -eq $embedded
}

function Assert-GameClosed($Installation) {
    $running = Get-Process -ErrorAction SilentlyContinue | Where-Object {
        try {
            $_.Path -and $_.Path.StartsWith(
                $Installation.GameRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)
        } catch { $false }
    }
    if ($running) { throw 'Close My Furry Protogen before continuing.' }
}

function Get-Payload($Config, $Edition, [string]$PayloadRoot) {
    $items = @{}
    foreach ($group in @(
        @{ Root = (Join-Path $PayloadRoot $Edition.name); Files = $Edition.files },
        @{ Root = (Join-Path $PayloadRoot 'common'); Files = $Config.runtime }
    )) {
        Assert-PlainPath $group.Root
        foreach ($item in $group.Files) {
            $path = [string]$item.path
            Assert-PackagePath $path
            if ($items.ContainsKey($path) -or $item.sha256 -notmatch '^[a-f0-9]{64}$') {
                throw "Invalid or duplicate package path: $path"
            }
            $items.Add($path, [pscustomobject]@{
                source = Get-SafePath $group.Root $path
                sha256 = [string]$item.sha256
            })
        }
    }
    foreach ($language in $Config.languages.PSObject.Properties) {
        if (-not $items.ContainsKey("game/tl/$($language.Value)/vnrevival_protogen_text.rpy")) {
            throw "Missing translation: $($language.Name)"
        }
    }
    return $items
}

function Install-Localization($Config, $Edition, $Installation, $Payload, $Owned, [string]$StateRoot, [string]$ReceiptPath) {
    $transaction = Join-Path $StateRoot 'transaction'
    $rollbackRoot = Join-Path $transaction 'rollback'
    $stageRoot = Join-Path $transaction 'staged'
    $plan = [Collections.Generic.List[object]]::new()
    $receiptFiles = [Collections.Generic.List[object]]::new()

    foreach ($relative in ($Payload.Keys | Sort-Object)) {
        $item = $Payload[$relative]
        $destination = Get-SafePath $Installation.GameRoot $relative
        $currentHash = Get-Sha256 $destination
        if ([IO.Directory]::Exists($destination)) {
            throw "The destination is not a regular file: $relative"
        }
        if ($currentHash -and $currentHash -ne $item.sha256 -and $currentHash -ne $Owned[$relative]) {
            throw "The file belongs to another patch or was edited: $relative"
        }
        if ($relative.EndsWith('.rpy')) {
            $compiled = Get-SafePath $Installation.GameRoot ($relative + 'c')
            if ([IO.Directory]::Exists($compiled) -or [IO.File]::Exists($compiled)) {
                if (-not $currentHash -or -not [IO.File]::Exists($compiled) -or
                    -not (Test-CompiledScript $compiled $destination)) {
                    throw "Existing Ren'Py bytecode could not be attributed to its source: $relative"
                }
                if ($currentHash -ne $item.sha256) {
                    $plan.Add(@{ path = $relative + 'c'; beforeSHA256 = Get-Sha256 $compiled; afterSHA256 = $null })
                }
            }
        }
        if ((Get-Sha256 $item.source) -ne $item.sha256) {
            throw "Package checksum failed: $relative. Extract the installer again."
        }
        $receiptFiles.Add(@{ path = $relative; installedSHA256 = $item.sha256 })
        if ($currentHash -ne $item.sha256) {
            $plan.Add(@{ path = $relative; beforeSHA256 = $currentHash; afterSHA256 = $item.sha256 })
        }
    }
    foreach ($relative in $Owned.Keys) {
        if (-not $Payload.ContainsKey($relative)) {
            throw "The previous package contains a file this installer cannot update: $relative"
        }
    }
    $receipt = Read-Receipt $ReceiptPath ([string]$Config.packageID)
    if ($plan.Count -eq 0 -and $receipt.edition -eq $Edition.name -and $receipt.version -eq $Config.version) { return }

    New-Item -ItemType Directory -Path $transaction | Out-Null
    $state = @{
        schemaVersion = 1; packageID = $Config.packageID; committed = $false
        previousReceiptSHA256 = Get-Sha256 $ReceiptPath
        files = $plan.ToArray()
    }
    try {
        foreach ($item in $plan) {
            $destination = Get-SafePath $Installation.GameRoot $item.path
            if ((Get-Sha256 $destination) -ne $item.beforeSHA256) { throw "The game changed during preparation: $($item.path)" }
            if ($item.beforeSHA256) {
                $backup = Get-SafePath $rollbackRoot $item.path
                [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($backup))
                [IO.File]::Copy($destination, $backup)
                if ((Get-Sha256 $backup) -ne $item.beforeSHA256) { throw "Backup failed: $($item.path)" }
            }
            if ($item.afterSHA256) {
                $stage = Get-SafePath $stageRoot $item.path
                [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($stage))
                [IO.File]::Copy($Payload[$item.path].source, $stage)
                if ((Get-Sha256 $stage) -ne $item.afterSHA256) { throw "Staging failed: $($item.path)" }
            }
        }
        if ($state.previousReceiptSHA256) {
            Copy-Item -LiteralPath $ReceiptPath -Destination (Join-Path $transaction 'previous-receipt.json')
        }
        Assert-GameClosed $Installation
        Write-JsonFile $state (Join-Path $transaction 'state.json')
        foreach ($item in $plan) {
            $destination = Get-SafePath $Installation.GameRoot $item.path
            if ((Get-Sha256 $destination) -ne $item.beforeSHA256) { throw "The game changed during installation: $($item.path)" }
            if ($item.afterSHA256) {
                [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination))
                Move-Item -LiteralPath (Get-SafePath $stageRoot $item.path) -Destination $destination -Force
            } else {
                Remove-Item -LiteralPath $destination
            }
            if ((Get-Sha256 $destination) -ne $item.afterSHA256) { throw "Installation verification failed: $($item.path)" }
        }
        Write-JsonFile @{
            schemaVersion = 1; packageID = $Config.packageID; version = $Config.version
            steamBuildID = $Installation.BuildId; edition = $Edition.name; files = $receiptFiles.ToArray()
        } $ReceiptPath
        $state.committed = $true
        Write-JsonFile $state (Join-Path $transaction 'state.json')
    } catch {
        Recover-Transaction $StateRoot $Installation.GameRoot $ReceiptPath
        throw
    }
    Recover-Transaction $StateRoot $Installation.GameRoot $ReceiptPath
}

$lock = $null
try {
    $configPath = Join-Path $BaseDirectory 'Resources/PackageConfig.json'
    $payloadRoot = Join-Path $BaseDirectory 'Resources/LocalizationPayload'
    Assert-PlainPath $configPath
    Assert-PlainPath $payloadRoot
    $config = [IO.File]::ReadAllText($configPath) | ConvertFrom-Json
    if ([int]$config.schemaVersion -ne 1 -or $config.steamAppID -ne $ExpectedAppId -or
        $config.packageID -ne 'fun.vnrevival.protogen' -or @($config.languages.PSObject.Properties).Count -ne 30) {
        throw 'The complete Protogen package could not be verified. Extract the installer again.'
    }
    $installation = Find-GameInstallation $GamePath
    $edition = Get-Edition $config $installation
    Assert-GameClosed $installation
    $payload = Get-Payload $config $edition $payloadRoot

    $stateRoot = Get-InstallationStateRoot $installation $StateRootOverride
    New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null
    Assert-PlainPath $stateRoot
    $lockPath = Join-Path $stateRoot 'install.lock'
    Assert-PlainPath $lockPath
    try { $lock = [IO.File]::Open($lockPath, 'OpenOrCreate', 'ReadWrite', 'None') }
    catch { throw 'Another Protogen installer is in progress, or its state folder is inaccessible.' }
    $receiptPath = Join-Path $stateRoot 'receipt.json'
    Assert-PlainPath $receiptPath
    Recover-Transaction $stateRoot $installation.GameRoot $receiptPath
    $receipt = Read-Receipt $receiptPath ([string]$config.packageID)
    $owned = Get-OwnedFiles $receipt

    if ($Launch) {
        if ($null -eq $receipt -or $receipt.edition -ne $edition.name) {
            throw 'Install the localization for the current game edition first.'
        }
        foreach ($relative in $payload.Keys) {
            if ($payload[$relative].sha256 -ne $owned[$relative] -or
                (Get-Sha256 (Get-SafePath $installation.GameRoot $relative)) -ne $owned[$relative]) {
                throw "The localized game needs a repair. Install the localization again. ($relative)"
            }
        }
        $runtime = Get-SafePath $installation.GameRoot '.vnrevival-protogen/runtime'
        $python = Join-Path $runtime 'lib/py3-windows-x86_64/pythonw.exe'
        $script = Join-Path $runtime 'renpy.py'
        Start-Process -FilePath $python -WorkingDirectory $installation.GameRoot -ArgumentList @(
            ('"{0}"' -f $script), ('"{0}"' -f $installation.GameRoot)
        ) | Out-Null
    } else {
        Install-Localization $config $edition $installation $payload $owned $stateRoot $receiptPath
    }
    Write-Status 'SUCCESS' $installation.GameRoot
    exit 0
} catch {
    Write-Status 'ERROR' $_.Exception.Message
    exit 1
} finally {
    if ($null -ne $lock) { $lock.Dispose() }
}
