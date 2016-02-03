@echo off
setlocal
rem
rem Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
rem COMPANY CONFIDENTIAL
rem
call %~dp0..\config\script\set_environment.bat

curl -X get http://admin:admin@172.28.161.145:8006/ifcr/sites/%ENDECA_PROJECT_NAME% > %ENDECA_PROJECT_DIR%\control\app_status.txt
find /i "pages" %ENDECA_PROJECT_DIR%\control\app_status.txt
if %errorlevel% equ 1 goto notfound
echo workbench is up - Checking File Size
goto checkFileSize

:notfound
echo workbench is down - abort baseline
goto done

:checkFileSize
call load_baseline_test_data.bat
call dimension_creation_py.bat
C:\Python27\python.exe %DIMPATH%\run.py 

:done
del %ENDECA_PROJECT_DIR%\control\app_status.txt
del %ENDECA_PROJECT_DIR%\test_data\baseline\*.txt
del D:\Endeca\apps\Data\*.txt
rem call archive_files.bat
 