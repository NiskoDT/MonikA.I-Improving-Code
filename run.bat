@echo off
ECHO.

ECHO Installing: numpy
"libs/pythonlib/python.exe" -m pip install numpy==1.23.0

ECHO.
ECHO Installing: playwright
"libs/pythonlib/python.exe" -m playwright install

ECHO.
ECHO Running now
"libs/pythonlib/python.exe" main.py
