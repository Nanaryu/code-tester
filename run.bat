@echo off
cd /d %~dp0
py -m pip install -r requirements.txt
cls
py -m code_tester
exit /b %errorlevel%
