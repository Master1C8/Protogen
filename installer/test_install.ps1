param(
    [Parameter(Mandatory = $true)][string]$Package,
    [Parameter(Mandatory = $true)][string]$BaseGame,
    [Parameter(Mandatory = $true)][string]$DlcGame,
    [Parameter(Mandatory = $true)][string]$Work
)
$ErrorActionPreference = 'Stop'
$Work = [IO.Path]::GetFullPath($Work)
if (Test-Path -LiteralPath $Work) { throw 'Use a fresh test folder.' }
$Package = [IO.Path]::GetFullPath($Package)
$config = Get-Content -Raw -LiteralPath (Join-Path $Package 'Resources/PackageConfig.json') | ConvertFrom-Json
$build = [string]$config.steamBuildID
$game = Join-Path $Work 'library/steamapps/common/My Furry Protogen'
$acf = Join-Path $Work 'library/steamapps/appmanifest_2009010.acf'
$state = Join-Path $Work 'state'
$status = Join-Path $Work 'status.txt'
$receipt = Join-Path $state 'receipt.json'
$hostExe = (Get-Process -Id $PID).Path
$utf8 = [Text.UTF8Encoding]::new($false)
New-Item -ItemType Directory -Path (Join-Path $game 'game/tl/None') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $game 'game/saves') -Force | Out-Null

function Assert($Condition, [string]$Description) {
    if (-not $Condition) { throw $Description }
}

function Hash([string]$Path) {
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}

function Set-Edition($Edition, [string]$Source) {
    [IO.File]::WriteAllText($acf, @"
"AppState" {
    "appid" "2009010"
    "buildid" "$build"
    "installdir" "My Furry Protogen"
}
"@, $utf8)
    foreach ($property in $Edition.original.PSObject.Properties) {
        Copy-Item -LiteralPath (Join-Path $Source $property.Name) -Destination (Join-Path $game $property.Name) -Force
    }
}

function Invoke-Install([string]$Expected, [string]$Detail = '', [string]$Source = $Package) {
    $appHelper = Join-Path $Source 'install.ps1'
    & $hostExe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $appHelper -BaseDirectory $Source `
        -GamePath $game -StatusFile $status -StateRootOverride $state
    $exitCode = $LASTEXITCODE
    $result = Get-Content -Raw -LiteralPath $status
    Assert ($result.StartsWith("$Expected`n") -and (($exitCode -eq 0) -eq ($Expected -eq 'SUCCESS'))) $result
    if ($Detail) { Assert ($result.Contains($Detail)) "Unexpected rejection: $result" }
    Write-Output "$Expected $Detail"
}

function Assert-Edition($Edition) {
    $installed = Get-Content -Raw -LiteralPath $receipt | ConvertFrom-Json
    Assert ($installed.edition -eq $Edition.name) 'Wrong installed edition.'
    $items = @($Edition.files) + @($config.runtime)
    Assert (@($installed.files).Count -eq $items.Count) 'Incomplete receipt.'
    foreach ($file in $items) {
        Assert ((Hash (Join-Path $game $file.path)) -eq $file.sha256) "Wrong installed file: $($file.path)"
    }
    foreach ($property in $Edition.original.PSObject.Properties) {
        Assert ((Hash (Join-Path $game $property.Name)) -eq $property.Value) "Original changed: $($property.Name)"
    }
}

$base = @($config.editions | Where-Object { $_.name -eq 'base' })[0]
$dlc = @($config.editions | Where-Object { $_.name -eq 'dlc' })[0]
$foreignFolder = Join-Path $game 'game/tl'
$foreign = Join-Path $foreignFolder 'other_mod.rpy'
$save = Join-Path $game 'game/saves/persistent'
[IO.File]::WriteAllText($foreign, '# foreign mod', $utf8)
[IO.File]::WriteAllText($save, 'player save marker', $utf8)
$foreignHash = Hash $foreign
$saveHash = Hash $save
Set-Edition $base $BaseGame

$relative = 'game/tl/russian/vnrevival_protogen_text.rpy'
$installedRussian = Join-Path $game $relative
New-Item -ItemType Directory -Path (Split-Path -Parent $installedRussian) | Out-Null
[IO.File]::WriteAllText($installedRussian, '# foreign same-name file', $utf8)
$sameNameHash = Hash $installedRussian
Invoke-Install ERROR 'belongs to another patch'
Assert ((Hash $installedRussian) -eq $sameNameHash) 'Foreign same-name file was replaced.'
Assert (-not (Test-Path -LiteralPath $receipt)) 'Refused install created a receipt.'
Remove-Item -LiteralPath $installedRussian

Invoke-Install SUCCESS
Assert-Edition $base
$firstReceipt = Hash $receipt
Invoke-Install SUCCESS
Assert ((Hash $receipt) -eq $firstReceipt) 'Idempotent install rewrote its receipt.'

# A matching compiled add-on is retired on a base-to-DLC update. An unowned file survives.
$compiled = $installedRussian + 'c'
$md5 = [Security.Cryptography.MD5]::Create()
try {
    $prefix = [Text.Encoding]::ASCII.GetBytes('RENPY RPC2')
    $footer = $md5.ComputeHash([IO.File]::ReadAllBytes($installedRussian))
    [IO.File]::WriteAllBytes($compiled, [byte[]]($prefix + $footer))
} finally { $md5.Dispose() }
Set-Edition $dlc $DlcGame
Invoke-Install SUCCESS
Assert-Edition $dlc
Assert (-not (Test-Path -LiteralPath $compiled)) 'Stale matching bytecode survived.'
Assert ((Hash $save) -eq $saveHash -and (Hash $foreign) -eq $foreignHash) 'Player data changed.'

$dlcReceipt = Hash $receipt
$corrupt = Join-Path $Work 'corrupt-package'
New-Item -ItemType Directory -Path (Join-Path $corrupt 'Resources/LocalizationPayload/dlc/game/tl/russian') -Force | Out-Null
$resources = Join-Path $Package 'Resources'
Copy-Item -LiteralPath (Join-Path $Package 'install.ps1') -Destination $corrupt
Copy-Item -LiteralPath (Join-Path $resources 'PackageConfig.json') -Destination (Join-Path $corrupt 'Resources')
$sourcePayload = Join-Path $resources 'LocalizationPayload'
$corruptPayload = Join-Path $corrupt 'Resources/LocalizationPayload'
Copy-Item -LiteralPath (Join-Path $sourcePayload 'dlc/game') -Recurse -Force -Destination (Join-Path $corruptPayload 'dlc')
Copy-Item -LiteralPath (Join-Path $sourcePayload 'common') -Recurse -Destination $corruptPayload
$payloadFile = Join-Path $corruptPayload ('dlc/' + $relative)
[IO.File]::WriteAllText($payloadFile, '# corrupted payload', $utf8)
Invoke-Install ERROR 'Package checksum failed' $corrupt
Assert ((Hash $receipt) -eq $dlcReceipt) 'Corrupt payload changed the receipt.'
Assert-Edition $dlc

# Simulate a crash after replacing one installed file but before committing its receipt.
$transaction = Join-Path $state 'transaction'
$backup = Join-Path $transaction ('rollback/' + $relative)
New-Item -ItemType Directory -Path (Split-Path -Parent $backup) -Force | Out-Null
Copy-Item -LiteralPath $installedRussian -Destination $backup
Copy-Item -LiteralPath $receipt -Destination (Join-Path $transaction 'previous-receipt.json')
$before = Hash $installedRussian
$new = Join-Path $Package ('Resources/LocalizationPayload/base/' + $relative)
Copy-Item -LiteralPath $new -Destination $installedRussian -Force
$journal = @{
    schemaVersion = 1; packageID = $config.packageID; committed = $false
    previousReceiptSHA256 = $dlcReceipt
    files = @(@{ path = $relative; beforeSHA256 = $before; afterSHA256 = (Hash $new) })
}
[IO.File]::WriteAllText((Join-Path $transaction 'state.json'), ($journal | ConvertTo-Json -Depth 5), $utf8)
Invoke-Install SUCCESS
Assert ((Hash $receipt) -eq $dlcReceipt) 'Recovery changed the previous receipt.'
Assert (-not (Test-Path -LiteralPath $transaction)) 'Transaction was not cleared.'
Assert-Edition $dlc

Set-Edition $base $BaseGame
Invoke-Install SUCCESS
Assert-Edition $base
Assert ((Hash $save) -eq $saveHash -and (Hash $foreign) -eq $foreignHash) 'Player data changed.'
Write-Output 'PASS: base, DLC, repeat, transitions, interrupted update recovery, collision, corrupt payload, protected files.'
