@echo off
setlocal
cd /d "%~dp0"
echo ============================================
echo   AItutor 一键安装
echo   （解压本项目后双击本文件即可）
echo ============================================
echo.
call "tools\setup\install.bat" %*
set EXIT_CODE=%ERRORLEVEL%
echo.
echo 一键安装结束（退出码：%EXIT_CODE%）
pause
exit /b %EXIT_CODE%