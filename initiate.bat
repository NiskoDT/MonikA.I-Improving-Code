@echo off
@REM ? Final file after Testing Commands.bat file

:start
ECHO.
ECHO Do you want to run the update first?
ECHO [Y] Yes, I want to update then run
ECHO [N] No, just run the file now
ECHO.
set /p choice=Type your choice (Y/N) 
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='Y' goto CYes
if '%choice%'=='y' goto CYes
if '%choice%'=='N' goto CNo
if '%choice%'=='n' goto CNo
ECHO.
ECHO The choice \"%choice%\" is not valid, try again
ECHO.
ECHO Press Ctrl + C now and then Y to quit
pause
goto start

:CYes
ECHO.
ECHO Okay! Running Update then Run...
ECHO.
call update.bat
ECHO.
call run.bat

:CNo
ECHO.
ECHO Okay! Running now...
ECHO.
call run.bat