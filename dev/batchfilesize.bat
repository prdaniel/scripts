@echo off

set items="C:\Endeca\apps\baseline\items.txt"
set minItems=60000000
set attributes="C:\Endeca\apps\baseline\attributes.txt"
set minAttr=10000000
set hierarchy="C:\Endeca\apps\baseline\hierarchy.txt"
set minHier=60000
set brand="C:\Endeca\apps\baseline\brands.txt"
set minBrand=6000000000

FOR /F "usebackq" %%A IN ('%items%') DO set sizeItems=%%~zA

	if %sizeItems% LSS %minItems% (
		echo.Items is ^< %minItems% bytes - Failed
		goto done
	)ELSE (
		echo.Items is ^>= %minItems% bytes %sizeItems% - Passed
		echo Checking attrbiutes.txt ....
		)
		
FOR /F "usebackq" %%A IN ('%attributes%') DO set sizeAttr=%%~zA

	if %sizeAttr% LSS %minAttr% (
		echo.Attributes is ^< %minAttr% bytes - Failed
		goto done
	)ELSE (
		echo.Attributes is ^>= %minAttr% bytes %sizeAttr% - Passed
		echo Checking hierarchy.txt ....
		)
			
FOR /F "usebackq" %%A IN ('%hierarchy%') DO set sizeHier=%%~zA

	if %sizeHier% LSS %minHier% (
		echo.Hierarchy is ^< %minHier% bytes - Failed
		goto done
	)ELSE (
		echo.Hierarchy is ^>= %minHier% bytes %sizeHier% - Passed
		echo Checking brands.txt ....
		)

FOR /F "usebackq" %%A IN ('%brand%') DO set sizeBrand=%%~zA

	if %sizeBrand% LSS %minBrand% (
		echo.Brand is ^< %minBrand% bytes - Failed
		goto done
	)ELSE (
		echo.Brand is ^>= %minBrand% bytes %sizeBrand% - Passed
		echo Checking Worbench Status ....
		)
:Done
echo Files are bad		