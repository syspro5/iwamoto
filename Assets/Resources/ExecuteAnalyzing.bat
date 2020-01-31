@echo off

echo Analyzing...
SET VideoPath=%1
SET OpenPoseDir=%2
SET LiftingDir=%3
rem SET SaveDir=%4

echo %OpenPoseDir%
echo %VideoPath%
echo %LiftingDir%

set dateData=%DATE:/=%%time:~0,2%%time:~3,2%%time:~6,2%


cd %OpenPoseDir%
call .\bin\OpenPoseDemo.exe --video %VideoPath% --write_json .\output\%dateData% rem --net_resolution 176x128 

echo finish outputting json


set path=%path%;c:\users\%username%\Anaconda3
set path=%path%;c:\users\%username%\Anaconda3\scripts

call conda activate TensGPU150
call python json2csv2.py .\output\%dateData%

echo finish outputting 2dpose


call python %LiftingDir%\applications\extract3dpose.py %OpenPoseDir%\output.csv C:\Users\%username%\Desktop\pose3ds%dateData%.csv
rem cd C:\Users\IWMTT\Lifting-from-the-Deep-release

rem call python .\applications\demo.py
rem call conda deactivate
echo finish outputting 3dpose

set ERRORLEVEL=C:\Users\%username%\Desktop\pose3ds%dateData%.csv

pause