@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
echo ============================================
echo   AItutor Sync (GitHub + Gitee + GitCode)
echo ============================================
echo.
echo [1/3] GitHub ...
git push origin master
echo.
echo [2/3] Gitee ...
git push gitee master
echo.
echo [3/3] GitCode ...
git push gitcode master
echo.
echo ============================================
echo   Sync finished.
echo ============================================
pause