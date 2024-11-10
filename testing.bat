@echo off
setlocal enabledelayedexpansion

set input_file=tests.txt

rem Olvasd be a fájl tartalmát és futtasd a python programot minden sorra
for /f "tokens=*" %%A in (%input_file%) do (
    set "line=%%A"
    if !line! neq "" (
        echo !line! > temp_input.txt
        python feladat2.py < temp_input.txt
        if errorlevel 1 (
            echo "Hiba történt"
            pause
            exit /b
        )
    )
)

del temp_input.txt
pause > nul
endlocal
