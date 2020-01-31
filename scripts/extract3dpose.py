#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 2020

Thanks to @original author: Denis Tome'
"""

import __init__

from lifting import PoseEstimator
from lifting.utils import draw_limbs
from lifting.utils import plot_pose

import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
from os.path import dirname, realpath
from copy import copy

DIR_PATH = dirname(realpath(__file__))
PROJECT_PATH = realpath(DIR_PATH + '/..')
IMAGE_FILE_PATH = PROJECT_PATH + '/data/images/mac.png'
SAVED_SESSIONS_DIR = PROJECT_PATH + '/data/saved_sessions'
SESSION_PATH = SAVED_SESSIONS_DIR + '/init_session/init'
PROB_MODEL_PATH = SAVED_SESSIONS_DIR + '/prob_model/prob_model_params.mat'

def csvReadGen(filename, header=True):
    import csv
    with open(filename,"r",encoding="utf-8") as f:
        reader = csv.reader((line.replace(' ', '').strip('\n') for line in f))
        
        if header:
            next(reader)
        
        for row in reader:
            yield row
        
            
def csvWriteGen(data):
    with open('output2.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(data)
 

def main():
    
    readFilename=sys.argv[1]

    ## omajinai
    image = cv2.imread(IMAGE_FILE_PATH)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # conversion to rgb
    ## create pose estimator
    image_size = image.shape
    ## omajinai


    pose_estimator = PoseEstimator(image_size, SESSION_PATH, PROB_MODEL_PATH)

    ## load model
    pose_estimator.initialise()
    ## filename="output.csv"
    itrLen = len(open(readFilename).readlines())-1
    gen = csvReadGen(readFilename)
    dataVisibility=[]
    dataPose_3d=[]
    for i in range(itrLen):
        tmpline = [float(s) for s in next(gen)]
        estimated_2d_pose, visibility = np.split(tmpline,[28])
        estimated_2d_pose = estimated_2d_pose.astype(np.int32)
        visibility = np.array([np.where(visibility>0.1,True,False)])
        
        try:
            e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12,e13,e14 = np.split(estimated_2d_pose.astype(np.int32),14)
            estimated_2d_pose=np.array([[np.array(e01),np.array(e02),np.array(e03),np.array(e04), \
                               np.array(e05),np.array(e06),np.array(e07),np.array(e08), \
                               np.array(e09),np.array(e10),np.array(e11),np.array(e12), \
                               np.array(e13),np.array(e14)]])
            visibility, pose_3d = pose_estimator.estimate3Dfrom2D(estimated_2d_pose, visibility)
            pose_3d[0,0] = -pose_3d[0,0] #x->x'
            pose_3dy = copy(pose_3d[0,1])
            pose_3dz = copy(pose_3d[0,2])
            pose_3d[0,1] = pose_3dz
            pose_3d[0,2] = -pose_3dy

            # calculate vector
            ## hips 2 upper Leg
            hips2uLR = np.array([ pose_3d[0,0,1] - pose_3d[0,0,0],pose_3d[0,1,1] - pose_3d[0,1,0],pose_3d[0,2,1] - pose_3d[0,2,0] ])
            hips2uLR = hips2uLR / np.linalg.norm(hips2uLR)
            hips2uLL = np.array([ pose_3d[0,0,4] - pose_3d[0,0,0],pose_3d[0,1,4] - pose_3d[0,1,0],pose_3d[0,2,4] - pose_3d[0,2,0] ])
            hips2uLL = hips2uLL / np.linalg.norm(hips2uLL)
            
            ## upper Leg 2 knee
            uL2kneeR = np.array([ pose_3d[0,0,2] - pose_3d[0,0,1],pose_3d[0,1,2] - pose_3d[0,1,1],pose_3d[0,2,2] - pose_3d[0,2,1] ])
            uL2kneeR = uL2kneeR / np.linalg.norm(uL2kneeR)
            uL2kneeL = np.array([ pose_3d[0,0,5] - pose_3d[0,0,4],pose_3d[0,1,5] - pose_3d[0,1,4],pose_3d[0,2,5] - pose_3d[0,2,4] ])
            uL2kneeL = uL2kneeL / np.linalg.norm(uL2kneeL)
            
            ## knee 2 foot
            knee2footR = np.array([ pose_3d[0,0,3] - pose_3d[0,0,2],pose_3d[0,1,3] - pose_3d[0,1,2],pose_3d[0,2,3] - pose_3d[0,2,2] ])
            knee2footR = knee2footR / np.linalg.norm(knee2footR)
            knee2footL = np.array([ pose_3d[0,0,6] - pose_3d[0,0,5],pose_3d[0,1,6] - pose_3d[0,1,5],pose_3d[0,2,6] - pose_3d[0,2,5] ])
            knee2footL = knee2footL / np.linalg.norm(knee2footL)
            
            ## spine 2 hips
            spine2hips = np.array([ pose_3d[0,0,0] - pose_3d[0,0,7],pose_3d[0,1,0] - pose_3d[0,1,7],pose_3d[0,2,0] - pose_3d[0,2,7] ])
            spine2hips = spine2hips / np.linalg.norm(spine2hips)
            
            ## spine 2 chest
            spine2chest = np.array([ pose_3d[0,0,8] - pose_3d[0,0,7],pose_3d[0,1,8] - pose_3d[0,1,7],pose_3d[0,2,8] - pose_3d[0,2,7] ])
            spine2chest = spine2chest / np.linalg.norm(spine2chest)
            
            ## chest 2 shoulder
            chest2shoulderR = np.array([ pose_3d[0,0,14] - pose_3d[0,0,8],pose_3d[0,1,14] - pose_3d[0,1,8],pose_3d[0,2,14] - pose_3d[0,2,8] ])
            chest2shoulderR = chest2shoulderR / np.linalg.norm(chest2shoulderR)
            chest2shoulderL = np.array([ pose_3d[0,0,11] - pose_3d[0,0,8],pose_3d[0,1,11] - pose_3d[0,1,8],pose_3d[0,2,11] - pose_3d[0,2,8] ])
            chest2shoulderL = chest2shoulderL / np.linalg.norm(chest2shoulderL)
            
            ## shoulder 2 elbow
            shoulder2elbowR = np.array([ pose_3d[0,0,15] - pose_3d[0,0,14],pose_3d[0,1,15] - pose_3d[0,1,14],pose_3d[0,2,15] - pose_3d[0,2,14] ])
            shoulder2elbowR = shoulder2elbowR / np.linalg.norm(shoulder2elbowR)
            shoulder2elbowL = np.array([ pose_3d[0,0,12] - pose_3d[0,0,11],pose_3d[0,1,12] - pose_3d[0,1,11],pose_3d[0,2,12] - pose_3d[0,2,11] ])
            shoulder2elbowL = shoulder2elbowL / np.linalg.norm(shoulder2elbowL)
            
            ## elbow 2 hand
            elbow2handR = np.array([ pose_3d[0,0,16] - pose_3d[0,0,15],pose_3d[0,1,16] - pose_3d[0,1,15],pose_3d[0,2,16] - pose_3d[0,2,15] ])
            elbow2handR = elbow2handR / np.linalg.norm(elbow2handR)
            elbow2handL = np.array([ pose_3d[0,0,13] - pose_3d[0,0,12],pose_3d[0,1,13] - pose_3d[0,1,12],pose_3d[0,2,13] - pose_3d[0,2,12] ])
            elbow2handL = elbow2handL / np.linalg.norm(elbow2handL)
            
            ## chest 2 chin
            chest2chin = np.array([ pose_3d[0,0,9] - pose_3d[0,0,8],pose_3d[0,1,9] - pose_3d[0,1,8],pose_3d[0,2,9] - pose_3d[0,2,8] ])
            chest2chin = chest2chin / np.linalg.norm(chest2chin)
            
            ## chin 2 head 
            chin2head = np.array([ pose_3d[0,0,10] - pose_3d[0,0,9],pose_3d[0,1,10] - pose_3d[0,1,9],pose_3d[0,2,10] - pose_3d[0,2,9] ])
            chin2head = chin2head / np.linalg.norm(chin2head)
            
            pose_3d = np.array([np.array([0.0,0.0,0.0]), \
            hips2uLR,uL2kneeR,knee2footR, \
            hips2uLL,uL2kneeL,knee2footL, \
            spine2hips,spine2chest,chest2chin,chin2head, \
            chest2shoulderL,shoulder2elbowL,elbow2handL, \
            chest2shoulderR,shoulder2elbowR,elbow2handR, \
            ])
            pose_3d = np.array([pose_3d.transpose()])
            
            # for single_3D in pose_3d:
                # plot_pose(single_3D)

            # plt.show()            
            pose_3d = np.concatenate([pose_3d[0,0],pose_3d[0,1],pose_3d[0,2]]).reshape((1,51))
            e08 = e08.astype(np.float32).reshape((1,2))
            
            # print("e08 debug")
            # print(e08[0])
            # print(type(e08[0]))
            dataPose_3d.append(np.hstack([pose_3d[0], e08[0,1], e08[0,0]]))
            #print(pose_3d)
            
            

            
        except ValueError:
            print('The 2d pose data could not be translated to 3d pose data in this frame.')
    pose_estimator.close()
    return dataPose_3d


if __name__ == '__main__':
    dataPose_3d = main()
    #sys.exit(main())
    print(dataPose_3d)
    writeFilename=sys.argv[2]
    np.savetxt(writeFilename,dataPose_3d,delimiter=',',fmt='%.5f')