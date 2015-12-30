@echo off
title py2exe

cd bade

:loop
echo.
echo -------------------------------------
echo press a key to proceed the building
pause>nul

if EXIST ..\build (
echo deleting build content...
rmdir ..\build /s /q
echo ...done

echo creating build folder...
mkdir ..\build
echo ...done
) else (
echo creating build folder...
mkdir ..\build
echo ...done
)

echo building...
python setup.py build > ../build/log.txt
echo ...done

echo you can find the log in build\log.txt

move build\program.exe ..\build\ >nul
rmdir build /s /q
goto loop