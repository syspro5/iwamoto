@echo off
SET WGET_EXE=C:\users\%username%\desktop\extLib\openpose\3rdparty\windows\wget\wget.exe
cd C:\users\%username%\desktop\extLib\Lifting-from-the-Deep-release
cd data
mkdir saved_sessions
cd saved_sessions


echo 'Downloading models...'

%WGET_EXE% -c http://visual.cs.ucl.ac.uk/pubs/liftingFromTheDeep/res/init_session.tar.gz -P %CD%
%WGET_EXE% -c http://visual.cs.ucl.ac.uk/pubs/liftingFromTheDeep/res/prob_model.tar.gz -P %CD%

echo 'Extracting models...'
tar -xvzf init_session.tar.gz
tar -xvzf prob_model.tar.gz
del init_session.tar.gz
del prob_model.tar.gz

rem pause