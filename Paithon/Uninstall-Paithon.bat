@echo off
REM Uninstall-Paithon.bat
SETLOCAL
SET PaithonDir=%~dp0

REM Check if the directory is in PATH
echo %PATH% | find /i "%PaithonDir%" >nul
if %errorlevel% equ 0 (
    echo Paithon uninstalled successfully. Restart your Command Prompt.
) else (
    echo Paithon is not currently installed.
)
ENDLOCAL
