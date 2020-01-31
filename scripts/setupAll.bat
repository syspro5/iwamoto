@echo off

cd  C:\Users\%username%\Desktop\extLib\openpose\models
SET WGET_EXE=C:\Users\%username%\Desktop\extLib\openpose\3rdparty\windows\wget\wget.exe

echo ------------------------- BODY, FACE AND HAND MODELS -------------------------
echo ----- Downloading body pose (COCO and MPI), face and hand models -----
SET OPENPOSE_URL=http://posefs1.perception.cs.cmu.edu/OpenPose/models/
SET POSE_FOLDER=pose/
SET FACE_FOLDER=face/
SET HAND_FOLDER=hand/

echo:
echo ------------------------- POSE MODELS -------------------------
echo Body (BODY_25)
set BODY_25_FOLDER=%POSE_FOLDER%body_25/
set BODY_25_MODEL=%BODY_25_FOLDER%pose_iter_584000.caffemodel
%WGET_EXE% -c %OPENPOSE_URL%%BODY_25_MODEL% -P %BODY_25_FOLDER%

echo Body (COCO)
SET COCO_FOLDER=%POSE_FOLDER%coco/
SET COCO_MODEL=%COCO_FOLDER%pose_iter_440000.caffemodel
%WGET_EXE% -c %OPENPOSE_URL%%COCO_MODEL% -P %COCO_FOLDER%

echo:
echo Body (MPI)
SET MPI_FOLDER=%POSE_FOLDER%mpi/
SET MPI_MODEL=%MPI_FOLDER%pose_iter_160000.caffemodel
%WGET_EXE% -c %OPENPOSE_URL%%MPI_MODEL% -P %MPI_FOLDER%
echo ----------------------- POSE DOWNLOADED -----------------------

echo:
echo ------------------------- FACE MODELS -------------------------
echo Face
SET FACE_MODEL=%FACE_FOLDER%pose_iter_116000.caffemodel
%WGET_EXE% -c %OPENPOSE_URL%%FACE_MODEL% -P %FACE_FOLDER%
echo ----------------------- FACE DOWNLOADED -----------------------

echo:
echo ------------------------- HAND MODELS -------------------------
echo Hand
SET HAND_MODEL=%HAND_FOLDER%pose_iter_102000.caffemodel
%WGET_EXE% -c %OPENPOSE_URL%%HAND_MODEL% -P %HAND_FOLDER%
echo ----------------------- HAND DOWNLOADED -----------------------


cd C:\Users\%username%\Desktop\extLib\openpose
%WGET_EXE% -c https://github.com/syspro5/iwamoto/blob/master/scripts/json2csv2.py -P %CD%



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

cd C:\users\%username%\desktop\extLib\Lifting-from-the-Deep-release\applications
%WGET_EXE% -c https://github.com/syspro5/iwamoto/blob/master/scripts/extract3dpose.py -P %CD%


cd C:\users\%username%\desktop\extLib\Lifting-from-the-Deep-release\packages\lifting
%WGET_EXE% -c https://github.com/syspro5/iwamoto/blob/master/scripts/_pose_estimator.py -P %CD%


echo %errorlevel% : If 0, setup was successful.

pause