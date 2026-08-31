@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0..\.."
echo ============================================
echo   AItutor One-Click Setup (Windows)
echo ============================================
echo.
echo Usage:
echo   install.bat              one-click install (China mirror)
echo   install.bat -CheckOnly   check only
echo   install.bat -Global      use international sources
echo.
echo AI harnesses are NOT detected; official sites are listed below.
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0bootstrap.ps1" %*
set EXIT_CODE=%ERRORLEVEL%
echo.
if /I not "%1"=="-CheckOnly" (
  echo === Install done. Running health check automatically... ===
  python tools\doctor.py
  set EXIT_CODE=%ERRORLEVEL%
)
echo.
echo ============================================
echo   Setup finished. Exit code: %EXIT_CODE%
echo   When doctor passes, start learning.
echo ============================================
pause
exit /b %EXIT_CODE%