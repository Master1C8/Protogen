#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <commctrl.h>
#include <shellapi.h>
#include <shlobj.h>
#include <wchar.h>

#define APP_TITLE L"My Furry Protogen | VN Revival"
#define IDI_APP 101
#define ID_PANEL 102
#define ID_INSTALL 1002
#define ID_PROGRESS 1003
#define ID_CHOOSE_GAME 1004
#define WM_INSTALL_COMPLETE (WM_APP + 1)

enum InstallState { STATE_READY, STATE_WORKING, STATE_SUCCESS, STATE_ERROR };

typedef struct {
    HWND window;
    BOOL launch;
    wchar_t gamePath[MAX_PATH];
} InstallRequest;

typedef struct {
    BOOL success;
    wchar_t message[1024];
} InstallResult;

static const COLORREF COLOR_WINDOW_BG = RGB(11, 19, 44);
static const COLORREF COLOR_ACCENT = RGB(255, 190, 77);
static const COLORREF COLOR_ACCENT_PRESSED = RGB(224, 149, 44);
static const COLORREF COLOR_CARD = RGB(23, 34, 62);
static const COLORREF COLOR_BORDER = RGB(54, 73, 107);
static const COLORREF COLOR_TEXT = RGB(244, 247, 255);
static const COLORREF COLOR_MUTED = RGB(184, 199, 223);
static const COLORREF COLOR_SUCCESS = RGB(139, 233, 197);
static const COLORREF COLOR_ERROR = RGB(255, 175, 170);

static HFONT headingFont;
static HFONT bodyFont;
static HFONT smallFont;
static HFONT brandFont;
static HICON appIcon;
static HBITMAP panelBitmap;
static HBRUSH cardBackground;
static BOOL ownsAppIcon;
static HWND installButton;
static HWND chooseGameButton;
static HWND progressBar;
static HWND statusLabel;
static HWINSTA interactiveWindowStation;
static HDESK interactiveDesktop;
static enum InstallState installState = STATE_READY;
static wchar_t statusMessage[1024] = L"Close the game before installing.";
static wchar_t selectedGamePath[MAX_PATH] = L"";
static BOOL launchInProgress;

static void setFont(HWND control, HFONT font) {
    SendMessageW(control, WM_SETFONT, (WPARAM)font, TRUE);
}

static void drawTextLine(HDC dc, HFONT font, COLORREF color, const wchar_t *text, RECT bounds, UINT format) {
    HFONT previous = (HFONT)SelectObject(dc, font);
    SetTextColor(dc, color);
    SetBkMode(dc, TRANSPARENT);
    DrawTextW(dc, text, -1, &bounds, format);
    SelectObject(dc, previous);
}

static const wchar_t *buttonLabel(void) {
    if (installState == STATE_WORKING) return launchInProgress ? L"Launching…" : L"Installing…";
    if (installState == STATE_SUCCESS) return L"Launch game";
    if (installState == STATE_ERROR) return L"Retry installation";
    return L"Install localization";
}

static void fillRectangle(HDC dc, RECT bounds, COLORREF color) {
    HBRUSH brush = CreateSolidBrush(color);
    FillRect(dc, &bounds, brush);
    DeleteObject(brush);
}

static void drawCard(HDC dc, RECT bounds, COLORREF background, COLORREF border, int radius) {
    HBRUSH brush = CreateSolidBrush(background);
    HPEN pen = CreatePen(PS_SOLID, 1, border);
    HGDIOBJ previousBrush = SelectObject(dc, brush);
    HGDIOBJ previousPen = SelectObject(dc, pen);
    RoundRect(dc, bounds.left, bounds.top, bounds.right, bounds.bottom, radius, radius);
    SelectObject(dc, previousBrush);
    SelectObject(dc, previousPen);
    DeleteObject(brush);
    DeleteObject(pen);
}

static void paintInterface(HWND window) {
    PAINTSTRUCT paint;
    HDC dc = BeginPaint(window, &paint);
    RECT client;
    GetClientRect(window, &client);
    fillRectangle(dc, client, COLOR_WINDOW_BG);
    if (panelBitmap) {
        HDC source = CreateCompatibleDC(dc);
        HGDIOBJ previous = SelectObject(source, panelBitmap);
        StretchBlt(dc, 0, 0, 310, client.bottom, source, 0, 0, 310, 520, SRCCOPY);
        SelectObject(source, previous);
        DeleteDC(source);
    }
    fillRectangle(dc, (RECT){310, 0, 312, client.bottom}, COLOR_ACCENT);
    drawTextLine(dc, brandFont, COLOR_ACCENT, L"VN REVIVAL",
        (RECT){24, 420, 286, 449}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);
    drawTextLine(dc, bodyFont, COLOR_TEXT, L"MY FURRY PROTOGEN",
        (RECT){24, 454, 286, 491}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);

    drawTextLine(dc, smallFont, COLOR_ACCENT, L"STEAM  /  WINDOWS x64",
        (RECT){350, 46, 772, 68}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);
    drawTextLine(dc, headingFont, COLOR_TEXT, L"Install localization",
        (RECT){348, 77, 772, 133}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);
    drawTextLine(dc, bodyFont, COLOR_MUTED, L"30 languages for the base game and official DLC.",
        (RECT){350, 143, 772, 203}, DT_LEFT | DT_WORDBREAK | DT_NOPREFIX);

    drawCard(dc, (RECT){350, 217, 772, 436}, COLOR_CARD, COLOR_BORDER, 24);
    drawTextLine(dc, smallFont, COLOR_ACCENT, L"INSTALLATION STATUS",
        (RECT){373, 236, 748, 261}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);
    drawTextLine(dc, smallFont, COLOR_MUTED, L"In the game, open Preferences → Language.",
        (RECT){350, 461, 772, 493}, DT_LEFT | DT_SINGLELINE | DT_VCENTER);
    EndPaint(window, &paint);
}

static void refreshInterface(HWND window) {
    SetWindowTextW(statusLabel, statusMessage);
    SetWindowTextW(installButton, buttonLabel());
    RedrawWindow(window, NULL, NULL, RDW_INVALIDATE | RDW_ALLCHILDREN);
}

static void drawButton(const DRAWITEMSTRUCT *item, BOOL primary) {
    BOOL pressed = (item->itemState & ODS_SELECTED) != 0;
    BOOL disabled = (item->itemState & ODS_DISABLED) != 0;
    COLORREF background = COLOR_CARD;
    if (primary) background = disabled ? COLOR_BORDER : (pressed ? COLOR_ACCENT_PRESSED : COLOR_ACCENT);
    else if (pressed) background = COLOR_BORDER;
    drawCard(item->hDC, item->rcItem, background, primary ? background : COLOR_BORDER, 12);
    RECT textBounds = item->rcItem;
    if (pressed) OffsetRect(&textBounds, 0, 1);
    drawTextLine(item->hDC, primary ? brandFont : smallFont,
        primary && !disabled ? COLOR_WINDOW_BG : COLOR_TEXT,
        primary ? buttonLabel() : L"Game folder…",
        textBounds, DT_CENTER | DT_SINGLELINE | DT_VCENTER | DT_NOPREFIX);
    if (item->itemState & ODS_FOCUS) {
        RECT focus = item->rcItem;
        InflateRect(&focus, -4, -4);
        DrawFocusRect(item->hDC, &focus);
    }
}

static void chooseGameFolder(HWND window) {
    BROWSEINFOW browse = {0};
    browse.hwndOwner = window;
    browse.lpszTitle = L"Choose the Steam folder for My Furry Protogen";
    browse.ulFlags = BIF_RETURNONLYFSDIRS | BIF_NEWDIALOGSTYLE;
    LPITEMIDLIST item = SHBrowseForFolderW(&browse);
    if (!item) return;
    wchar_t path[MAX_PATH];
    BOOL resolved = SHGetPathFromIDListW(item, path);
    CoTaskMemFree(item);
    if (!resolved) {
        installState = STATE_ERROR;
        wcscpy_s(statusMessage, 1024, L"The selected folder could not be read.");
        refreshInterface(window);
        return;
    }
    wcsncpy_s(selectedGamePath, MAX_PATH, path, _TRUNCATE);
    installState = STATE_READY;
    wcscpy_s(statusMessage, 1024, L"Game folder selected. Ready to install.");
    refreshInterface(window);
}

static BOOL getModuleDirectory(wchar_t *buffer, DWORD count) {
    DWORD length = GetModuleFileNameW(NULL, buffer, count);
    if (length == 0 || length >= count) return FALSE;
    wchar_t *slash = wcsrchr(buffer, L'\\');
    if (!slash) return FALSE;
    *slash = L'\0';
    return TRUE;
}

static BOOL readUtf8File(const wchar_t *path, wchar_t *output, DWORD outputCount) {
    HANDLE file = CreateFileW(path, GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (file == INVALID_HANDLE_VALUE) return FALSE;
    DWORD size = GetFileSize(file, NULL);
    if (size == INVALID_FILE_SIZE || size == 0 || size > 64 * 1024) {
        CloseHandle(file);
        return FALSE;
    }
    char *bytes = (char *)HeapAlloc(GetProcessHeap(), 0, size + 1);
    if (!bytes) {
        CloseHandle(file);
        return FALSE;
    }
    DWORD read = 0;
    BOOL ok = ReadFile(file, bytes, size, &read, NULL);
    CloseHandle(file);
    if (!ok) {
        HeapFree(GetProcessHeap(), 0, bytes);
        return FALSE;
    }
    int converted = MultiByteToWideChar(CP_UTF8, 0, bytes, (int)read,
        output, (int)outputCount - 1);
    HeapFree(GetProcessHeap(), 0, bytes);
    if (converted <= 0) return FALSE;
    output[converted] = L'\0';
    return TRUE;
}

static DWORD WINAPI installWorker(LPVOID parameter) {
    InstallRequest *request = (InstallRequest *)parameter;
    InstallResult *result = (InstallResult *)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY,
        sizeof(InstallResult));
    if (!result) {
        PostMessageW(request->window, WM_INSTALL_COMPLETE, 0, 0);
        HeapFree(GetProcessHeap(), 0, request);
        return 1;
    }
    wchar_t baseDirectory[MAX_PATH], temporaryDirectory[MAX_PATH], statusPath[MAX_PATH];
    wchar_t systemDirectory[MAX_PATH], powershell[MAX_PATH], script[MAX_PATH];
    wchar_t commandLine[4096];
    if (!getModuleDirectory(baseDirectory, MAX_PATH)
        || !GetTempPathW(MAX_PATH, temporaryDirectory)
        || !GetTempFileNameW(temporaryDirectory, L"vnr", 0, statusPath)
        || !GetSystemDirectoryW(systemDirectory, MAX_PATH)) {
        wcscpy_s(result->message, 1024, L"Could not prepare the installation process.");
        PostMessageW(request->window, WM_INSTALL_COMPLETE, 0, (LPARAM)result);
        HeapFree(GetProcessHeap(), 0, request);
        return 1;
    }
    DeleteFileW(statusPath);
    _snwprintf_s(powershell, MAX_PATH, _TRUNCATE,
        L"%ls\\WindowsPowerShell\\v1.0\\powershell.exe", systemDirectory);
    _snwprintf_s(script, MAX_PATH, _TRUNCATE, L"%ls\\install.ps1", baseDirectory);
    _snwprintf_s(commandLine, 4096, _TRUNCATE,
        L"\"%ls\" -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File \"%ls\""
        L" -BaseDirectory \"%ls\" -StatusFile \"%ls\"%ls",
        powershell, script, baseDirectory, statusPath, request->launch ? L" -Launch" : L"");
    if (request->gamePath[0]) {
        size_t offset = wcslen(commandLine);
        _snwprintf_s(commandLine + offset, 4096 - offset, _TRUNCATE,
            L" -GamePath \"%ls\"", request->gamePath);
    }

    STARTUPINFOW startup = {0};
    PROCESS_INFORMATION process = {0};
    startup.cb = sizeof(startup);
    BOOL created = CreateProcessW(powershell, commandLine, NULL, NULL, FALSE,
        CREATE_NO_WINDOW, NULL, baseDirectory, &startup, &process);
    if (!created) {
        wcscpy_s(result->message, 1024, L"Could not start Windows PowerShell.");
    } else {
        WaitForSingleObject(process.hProcess, INFINITE);
        DWORD exitCode = 1;
        GetExitCodeProcess(process.hProcess, &exitCode);
        CloseHandle(process.hThread);
        CloseHandle(process.hProcess);
        wchar_t status[2048];
        if (!readUtf8File(statusPath, status, 2048)) {
            wcscpy_s(result->message, 1024, L"The installer ended without a status report.");
        } else if (exitCode == 0 && wcsncmp(status, L"SUCCESS\n", 8) == 0) {
            result->success = TRUE;
            wcscpy_s(result->message, 1024,
                request->launch ? L"The localized game is starting." :
                L"Localization installed. Choose your language in the game.");
        } else if (wcsncmp(status, L"ERROR\n", 6) == 0) {
            wcsncpy_s(result->message, 1024, status + 6, _TRUNCATE);
        } else {
            wcsncpy_s(result->message, 1024, status, _TRUNCATE);
        }
    }
    DeleteFileW(statusPath);
    PostMessageW(request->window, WM_INSTALL_COMPLETE, 0, (LPARAM)result);
    HeapFree(GetProcessHeap(), 0, request);
    return 0;
}

static void beginInstall(HWND window, BOOL launch) {
    InstallRequest *request = (InstallRequest *)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY,
        sizeof(InstallRequest));
    if (!request) {
        installState = STATE_ERROR;
        wcscpy_s(statusMessage, 1024, L"Could not allocate the installation request.");
        refreshInterface(window);
        return;
    }
    request->window = window;
    request->launch = launch;
    wcsncpy_s(request->gamePath, MAX_PATH, selectedGamePath, _TRUNCATE);
    HANDLE thread = CreateThread(NULL, 0, installWorker, request, 0, NULL);
    if (!thread) {
        HeapFree(GetProcessHeap(), 0, request);
        installState = STATE_ERROR;
        wcscpy_s(statusMessage, 1024, L"Could not start the installation worker.");
        refreshInterface(window);
        return;
    }
    CloseHandle(thread);
    launchInProgress = launch;
    installState = STATE_WORKING;
    wcscpy_s(statusMessage, 1024,
        launch ? L"Checking the installation and launching…" : L"Verifying and installing all 30 languages…");
    EnableWindow(chooseGameButton, FALSE);
    EnableWindow(installButton, FALSE);
    ShowWindow(progressBar, SW_SHOW);
    SendMessageW(progressBar, PBM_SETMARQUEE, TRUE, 30);
    refreshInterface(window);
}

static LRESULT CALLBACK windowProcedure(HWND window, UINT message, WPARAM wParam, LPARAM lParam) {
    switch (message) {
        case WM_CREATE: {
            headingFont = CreateFontW(-42, 0, 0, 0, FW_SEMIBOLD, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, DEFAULT_PITCH, L"Segoe UI");
            bodyFont = CreateFontW(-22, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, DEFAULT_PITCH, L"Segoe UI");
            smallFont = CreateFontW(-17, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, DEFAULT_PITCH, L"Segoe UI");
            brandFont = CreateFontW(-18, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, DEFAULT_PITCH, L"Segoe UI");
            cardBackground = CreateSolidBrush(COLOR_CARD);
            statusLabel = CreateWindowW(L"STATIC", statusMessage,
                WS_CHILD | WS_VISIBLE | SS_LEFT | SS_NOPREFIX | SS_EDITCONTROL,
                373, 273, 375, 77, window, NULL, NULL, NULL);
            setFont(statusLabel, smallFont);
            chooseGameButton = CreateWindowW(L"BUTTON", L"Game folder…",
                WS_CHILD | WS_VISIBLE | WS_TABSTOP | BS_OWNERDRAW,
                373, 364, 140, 46, window, (HMENU)ID_CHOOSE_GAME, NULL, NULL);
            setFont(chooseGameButton, smallFont);
            installButton = CreateWindowW(L"BUTTON", L"Install localization",
                WS_CHILD | WS_VISIBLE | WS_TABSTOP | BS_OWNERDRAW,
                525, 364, 224, 46, window, (HMENU)ID_INSTALL, NULL, NULL);
            setFont(installButton, bodyFont);
            progressBar = CreateWindowExW(0, PROGRESS_CLASSW, NULL,
                WS_CHILD | PBS_MARQUEE | PBS_SMOOTH,
                373, 346, 376, 6, window, (HMENU)ID_PROGRESS, NULL, NULL);
            return 0;
        }
        case WM_PAINT:
            paintInterface(window);
            return 0;
        case WM_ERASEBKGND:
            return 1;
        case WM_CTLCOLORSTATIC:
            if ((HWND)lParam == statusLabel) {
                COLORREF color = COLOR_MUTED;
                if (installState == STATE_SUCCESS) color = COLOR_SUCCESS;
                if (installState == STATE_ERROR) color = COLOR_ERROR;
                SetTextColor((HDC)wParam, color);
                SetBkColor((HDC)wParam, COLOR_CARD);
                return (LRESULT)cardBackground;
            }
            break;
        case WM_DRAWITEM:
            if ((UINT)wParam == ID_INSTALL || (UINT)wParam == ID_CHOOSE_GAME) {
                drawButton((const DRAWITEMSTRUCT *)lParam, (UINT)wParam == ID_INSTALL);
                return TRUE;
            }
            break;
        case WM_COMMAND:
            if (HIWORD(wParam) == BN_CLICKED && installState != STATE_WORKING) {
                if (LOWORD(wParam) == ID_INSTALL) {
                    beginInstall(window, installState == STATE_SUCCESS);
                    return 0;
                }
                if (LOWORD(wParam) == ID_CHOOSE_GAME) {
                    chooseGameFolder(window);
                    return 0;
                }
            }
            break;
        case WM_INSTALL_COMPLETE: {
            InstallResult *result = (InstallResult *)lParam;
            SendMessageW(progressBar, PBM_SETMARQUEE, FALSE, 0);
            ShowWindow(progressBar, SW_HIDE);
            EnableWindow(chooseGameButton, TRUE);
            EnableWindow(installButton, TRUE);
            installState = result && result->success ? STATE_SUCCESS : STATE_ERROR;
            wcsncpy_s(statusMessage, 1024,
                result ? result->message : L"Could not allocate the installer result.", _TRUNCATE);
            if (result) HeapFree(GetProcessHeap(), 0, result);
            refreshInterface(window);
            SetFocus(installButton);
            return 0;
        }
        case WM_CLOSE:
            if (installState == STATE_WORKING) {
                MessageBeep(MB_ICONINFORMATION);
                wcscpy_s(statusMessage, 1024,
                    L"Installation is in progress. Keep this window open until it finishes.");
                refreshInterface(window);
                return 0;
            }
            DestroyWindow(window);
            return 0;
        case WM_DESTROY:
            DeleteObject(headingFont);
            DeleteObject(bodyFont);
            DeleteObject(smallFont);
            DeleteObject(brandFont);
            DeleteObject(panelBitmap);
            DeleteObject(cardBackground);
            if (appIcon && ownsAppIcon) DestroyIcon(appIcon);
            PostQuitMessage(0);
            return 0;
    }
    return DefWindowProcW(window, message, wParam, lParam);
}

int WINAPI wWinMain(HINSTANCE instance, HINSTANCE previous, PWSTR commandLine, int showCommand) {
    (void)previous;
    (void)commandLine;
    (void)showCommand;
    INITCOMMONCONTROLSEX controls = { sizeof(controls), ICC_STANDARD_CLASSES | ICC_PROGRESS_CLASS };
    InitCommonControlsEx(&controls);
    interactiveWindowStation = OpenWindowStationW(L"WinSta0", FALSE, WINSTA_ALL_ACCESS);
    if (interactiveWindowStation) {
        SetProcessWindowStation(interactiveWindowStation);
        interactiveDesktop = OpenDesktopW(L"Default", 0, FALSE, MAXIMUM_ALLOWED);
        if (interactiveDesktop) SetThreadDesktop(interactiveDesktop);
    }
    HRESULT oleResult = OleInitialize(NULL);
    appIcon = (HICON)LoadImageW(instance, MAKEINTRESOURCEW(IDI_APP), IMAGE_ICON,
        256, 256, LR_DEFAULTCOLOR);
    ownsAppIcon = appIcon != NULL;
    panelBitmap = LoadBitmapW(instance, MAKEINTRESOURCEW(ID_PANEL));
    if (!appIcon) appIcon = LoadIconW(NULL, IDI_APPLICATION);

    WNDCLASSEXW windowClass = {0};
    windowClass.cbSize = sizeof(windowClass);
    windowClass.lpfnWndProc = windowProcedure;
    windowClass.hInstance = instance;
    windowClass.hCursor = LoadCursorW(NULL, IDC_ARROW);
    windowClass.hIcon = appIcon;
    windowClass.hIconSm = appIcon;
    windowClass.hbrBackground = NULL;
    windowClass.lpszClassName = L"VNRevivalProtogenInstaller";
    if (!RegisterClassExW(&windowClass)) return 1;
    DWORD style = WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX | WS_CLIPCHILDREN;
    RECT bounds = {0, 0, 810, 520};
    AdjustWindowRectEx(&bounds, style, FALSE, WS_EX_CONTROLPARENT);
    HWND window = CreateWindowExW(WS_EX_CONTROLPARENT, windowClass.lpszClassName, APP_TITLE,
        style, CW_USEDEFAULT, CW_USEDEFAULT, bounds.right - bounds.left, bounds.bottom - bounds.top,
        NULL, NULL, instance, NULL);
    if (!window) return 2;
    ShowWindow(window, SW_SHOWNORMAL);
    SetFocus(installButton);
    UpdateWindow(window);
    MSG message;
    while (GetMessageW(&message, NULL, 0, 0) > 0) {
        if (!IsDialogMessageW(window, &message)) {
            TranslateMessage(&message);
            DispatchMessageW(&message);
        }
    }
    if (interactiveDesktop) CloseDesktop(interactiveDesktop);
    if (interactiveWindowStation) CloseWindowStation(interactiveWindowStation);
    if (SUCCEEDED(oleResult)) OleUninitialize();
    return (int)message.wParam;
}
