@echo off

set buildScriptPath=%cd%\build.py
cd %~dp0
cd ..
cd python

start python.exe %buildScriptPath%"