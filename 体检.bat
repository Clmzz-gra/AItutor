@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
echo ========== AItutor Health Check ==========
echo Review output below; fix any [NEED-FIX] items.
echo.
python tools\doctor.py
set EXIT_CODE=%ERRORLEVEL%
echo.
echo ========== Health check finished. Exit code: %EXIT_CODE% ==========
echo If all [OK], you can start learning.
pause
exit /b %EXIT_CODE%