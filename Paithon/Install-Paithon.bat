@echo off
REM Install-Paithon.bat
SETLOCAL
SET PaithonDir=%~dp0

REM Check if the directory is already in PATH
echo %PATH% | find /i "%PaithonDir%" >nul
if %errorlevel% equ 0 (
    echo Paithon is already installed.
) else (
    REM Add Paithon directory to PATH
    setx PATH "%PATH%;%PaithonDir%"
    echo Paithon installed successfully. Restart your Command Prompt to use 'paithon' command.
)
ENDLOCAL
