@echo off

set zipPath='%cd%\python.zip'
cd %~dp0
cd ..
set decompPath='%cd%\python'

echo Python environment decompiling !
powershell -Command "Expand-Archive %zipPath% -DestinationPath %decompPath% -Force"
echo Done !
pause