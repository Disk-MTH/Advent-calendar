@echo off

set buildScriptPath=%MYFILES%

cd ..
cd python

start /wait python.exe "%buildScriptPath%\build.py"