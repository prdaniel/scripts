@echo off
if exist "C:\Endeca\apps\tmi20080311\test_data\baseline\data.done" (
    echo New Files Exist - Running OnDemand Baseline Update > "C:\Endeca\apps\tmi20080311\test_data\baseline\onDemandUpdate.log"
	call C:\Endeca\apps\tmi20080311\control\nightly_baseline.bat
	call sleep 30
	call C:\Endeca\apps\tmi20080311prod\control\run_complete_refresh.bat
	del "C:\Endeca\apps\tmi20080311\test_data\baseline\data.done"
) else (
    echo No new data files. > "C:\Endeca\apps\tmi20080311\test_data\baseline\onDemandUpdate.log"
)