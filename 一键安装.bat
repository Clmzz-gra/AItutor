@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
echo ============================================
echo   AItutor One-Click Setup
echo   (Unzip this project, then double-click this file)
echo ============================================
echo.
call "tools\setup\install.bat" %*
set EXIT_CODE=%ERRORLEVEL%
echo.
echo Setup finished. Exit code: %EXIT_CODE%
pause
exit /b %EXIT_CODE%