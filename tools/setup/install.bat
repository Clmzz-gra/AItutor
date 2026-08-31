@echo off
setlocal
cd /d "%~dp0..\.."

echo ============================================
echo   AItutor 一键环境安装（Windows）
echo ============================================
echo.
echo 用法:
echo   install.bat             一键安装缺失项（国内加速，不翻墙）
echo   install.bat -CheckOnly  只体检，不安装
echo   install.bat -Global     走国际官方源
echo.
echo 默认推荐 ZCode；Claude Code / Codex 按需手动安装。
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0bootstrap.ps1" %*
set EXIT_CODE=%ERRORLEVEL%
echo.
if /I not "%1"=="-CheckOnly" (
  echo === 安装完成，正在自动运行体检（doctor）... ===
  python tools\doctor.py
  set EXIT_CODE=%ERRORLEVEL%
)

echo.
echo ============================================
echo   一键安装脚本已结束（退出码：%EXIT_CODE%）
echo   下一步：python tools\doctor.py 自检
echo   doctor 通过后，对 AI 说：开始学习〈学科名〉
echo ============================================
pause
exit /b %EXIT_CODE%