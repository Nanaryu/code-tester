@echo off
py -m pip install -r requirements.txt
cls
py -m code_tester
exit /b %errorlevel%
