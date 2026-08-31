@echo off
cd /d "%~dp0"
streamlit run main.py --server.port 8502
pause
