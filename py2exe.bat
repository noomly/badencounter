@echo off
title py2exe

cd bade

:loop
echo.
echo -------------------------------------
echo press a key to proceed the building process or exit by pressing CTRL+C
pause>nul

if EXIST ..\build (
echo deleting build content...
rmdir ..\build /s /q

echo creating build folder...
mkdir ..\build
) else (
echo creating build folder...
mkdir ..\build
)

echo building...
python setup.py build > ../build/log.txt

echo moving bade/build/program.exe to actual build dir...
move build\program.exe ..\build\ >nul
rmdir build /s /q

echo copying level file to build dir...
mkdir ..\build\game
copy game\level.map ..\build\game\level.map >nul

echo copying res folder to build dir...
mkdir ..\build\res
copy res ..\build\res >nul
del ..\build\res\__init__.py

echo DONE - you can find the log in build\log.txt
goto loop
