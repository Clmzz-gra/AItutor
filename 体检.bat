@echo off
setlocal
cd /d "%~dp0"
echo ========== AItutor 体检 ==========
echo 运行后请查看是否有 [需处理] 项，并按提示修复。
echo.
python tools\doctor.py
set EXIT_CODE=%ERRORLEVEL%
echo.
echo ========== 体检结束（退出码：%EXIT_CODE%） ==========
echo 若全部 [OK]，就可以对 AI 说：开始学习〈学科名〉
pause
exit /b %EXIT_CODE%