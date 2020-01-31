import json
import pandas as pd
import numpy as np
import glob
import csv
import sys
 
def getFileName(path):
    filelist = glob.glob(path + "/*")
    return filelist
 
def getSpecificData(filelist):
    for i in range(len(filelist)):
        with open(filelist[i]) as f:
            try:
                data = json.load(f)
                data = np.array(data['people'][0]['pose_keypoints_2d']).reshape(-1,3)
                df = pd.DataFrame(data, columns=['X','Y','P'], index=["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", \
                "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel"])
 
                # select wanted data
                writeCSV([ \
                # float(df.at["MidHip", "X"]), float(df.at["MidHip", "Y"]), float(df.at["MidHip", "P"]), \
                float(df.at["Nose", "Y"]), float(df.at["Nose", "X"]), \
                float(df.at["Neck", "Y"]), float(df.at["Neck", "X"]), \
                float(df.at["RShoulder", "Y"]), float(df.at["RShoulder", "X"]), \
                float(df.at["RElbow", "Y"]), float(df.at["RElbow", "X"]), \
                float(df.at["RWrist", "Y"]), float(df.at["RWrist", "X"]), \
                float(df.at["LShoulder", "Y"]), float(df.at["LShoulder", "X"]), \
                float(df.at["LElbow", "Y"]), float(df.at["LElbow", "X"]), \
                float(df.at["LWrist", "Y"]), float(df.at["LWrist", "X"]), \
                float(df.at["RHip", "Y"]), float(df.at["RHip", "X"]), \
                float(df.at["RKnee", "Y"]), float(df.at["RKnee", "X"]), \
                float(df.at["RAnkle", "Y"]), float(df.at["RAnkle", "X"]), \
                float(df.at["LHip", "Y"]), float(df.at["LHip", "X"]), \
                float(df.at["LKnee", "Y"]), float(df.at["LKnee", "X"]), \
                float(df.at["LAnkle", "Y"]), float(df.at["LAnkle", "X"]), \
                float(df.at["Nose", "P"]), float(df.at["Neck", "P"]), \
                float(df.at["RShoulder", "P"]), float(df.at["RElbow", "P"]), float(df.at["RWrist", "P"]), \
                float(df.at["LShoulder", "P"]), float(df.at["LElbow", "P"]), float(df.at["LWrist", "P"]), \
                float(df.at["RHip", "P"]), float(df.at["RKnee", "P"]), float(df.at["RAnkle", "P"]), \
                float(df.at["LHip", "P"]), float(df.at["LKnee", "P"]), float(df.at["LAnkle", "P"]) \
                ])
            except:
                print("There are no 2d-pose. Compensated previous 2d-pose")
                

 
 
def writeCSV(data):
    with open('output.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(data)
 
def main():
    filelist = getFileName(sys.argv[1])
    with open('output.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n') 
        # col name
        writer.writerow([ \
        # "MidHip_x","MidHip_y","MidHip_w", \
        "Nose_y","Nose_x", \
        "Neck_y","Neck_x", \
        "RShoulder_x","RShoulder_y", \
        "RElbow_x","RElbow_y", \
        "RWrist_x","RWrist_y", \
        "LShoulder_x","LShoulder_y", \
        "LElbow_x","LElbow_y", \
        "LWrist_x","LWrist_y", \
        "RHip_y","RHip_x", \
        "RKnee_y","RKnee_x", \
        "RAnkle_y","RAnkle_x", \
        "LHip_y","LHip_x", \
        "LKnee_y","LKnee_x", \
        "LAnkle_y","LAnkle_x", \
        "Nose_w", "Neck_w", \
        "RShoulder_w", "RElbow_w", "RWrist_w", \
        "LShoulder_w", "LElbow_w", "LWrist_w", \
        "RHip_w", "RKnee_w", "RAnkle_w", \
        "LHip_w", "LKnee_w", "LAnkle_w", \
        ])
    getSpecificData(filelist)
 
if __name__ == '__main__':
    main()