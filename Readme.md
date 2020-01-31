# Making motion from a single raw RGB video by using "Openpose" and "Lifting from the Deep"

This project is licensed under the terms of the GNU GPLv3 license. By using the software, you are agreeing to the terms of the license agreement ([link](https://github.com/DenisTome/Lifting-from-the-Deep-release/blob/master/LICENSE)).

## Hardware Requirements
- Windows10(64-bit) machine
- Nvidia's GPU which  supports CUDA.


## Software Requirements
- [Python3.X](https://www.python.org/) (We recommend that you install the same version as latest Anaconda3)
- [Anaconda3](https://www.anaconda.com/) and virtual environment
- [CUDA toolkit v9.0](https://developer.nvidia.com/cuda-90-download-archive)
- [CUDNN 7.0.5](https://developer.nvidia.com/rdp/cudnn-archive)
- [Openpose v1.4.0](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/tag/v1.4.0)
- [Lifting from the Deep](https://github.com/DenisTome/Lifting-from-the-Deep-release)

## How to setup
### Install python3.X

### Install Anaconda3
Download 64-bit installer from [Anaconda.com/downloads](https://www.anaconda.com/distribution/).

When you install, we recommend that you add Anaconda to user PATH environment variable.

### Set up virtual environment for estimation
Open anaconda prompt and enter below.

```
conda create -n TensGPU150 python==3.6
conda activate TensGPU150
conda install scipy
conda install opencv
conda install matplotlib
pip install tensorflow-gpu==1.5.0
pip install scikit-image
```

If you added Anaconda to user PATH, you can this setup by running CondaSetupGPU.bat.

### Install CUDA toolkit
Get win64 installer from [cuda-90-download-archive](https://developer.nvidia.com/cuda-90-download-archive).
Install the software according to instructions.

### Install CUDNN 7.0.5
Go to [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive) .

You will be required to login or join nvidia's developer program then follow the instructions.

 Logging in with social account is easy way.

![](https://github.com/syspro5/iwamoto/blob/master/img/cudnn.png)

After logging in, find [cuDNN v7.0.5 for CUDA 9.0] and download library for windows10.

 (the other virsion might work but not sure :))

Unzip the file and add all contents to your CUDA toolkit install folder

 (usually `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0`).

### Get Openpose and Lifting from the Deep
Go to [openpose/releases/tag/v1.4.0](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/tag/v1.4.0) and get 64bit-gpu-binaries zip file.



### Get Lifting from the Deep
Download zip file from [Lifting-from-the-Deep-release](https://github.com/DenisTome/Lifting-from-the-Deep-release).


### Set up "extLib" folder
Create "extLib" folder on your Desktop and unzip openpose and lifting-from-the-deep as below.

(Please rename openpose dir)

```
c:
　├ users/
　│　└ (your user dir)/
　│　　　└ Desktop/
　│　　　　　　└ extLib/
　│　　　　　　　　　├ openpose/
　│　　　　　　　　　│     ├ 3rdparty/
　│　　　　　　　　　│     ├ bin/
　│　　　　　　　　　│     └ ︙
　│　　　　　　　　　│
　│　　　　　　　　　└ Lifting-from-the-Deep-release/
　│　　　　　　　　　      ├ applications/
　│　　　　　　　　　      ├ data/
　│　　　　　　　　　      └ ︙
　︙
```

Then, run `scripts/setupAll.bat` in our project .




**notice** If you want put extLib folder on the another location, you should edit some file.

Edit setupAll.bat(scripts/), AnalyzeButton.cs(Assets/), ExecuteAnalyzing.bat(Assets/Resources) if you want to change the location.

## Usage
1:Input video file path into the field and push Analyze button.

Then 3d pose data "pose3dsyyyymmddhhmmss.csv" will be generated on your desktop.

2:Input the 3d pose data path in the field and push Animate button.

![](https://github.com/syspro5/iwamoto/blob/master/img/screen.png)
