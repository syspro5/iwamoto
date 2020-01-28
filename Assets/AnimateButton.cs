using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using System;
using System.Diagnostics;

public class AnimateButton : MonoBehaviour
{
    //string strBatFilePath;
    string strposeDataPath;
    //public InputField batFilePath;
    public InputField poseDataPath;

    GameObject controller;
    csv2pose script;


    public void whenPressed()
    {
        controller = GameObject.Find("controller");
        script = controller.GetComponent<csv2pose>();
        
        strposeDataPath = poseDataPath.text;
        if (strposeDataPath != "")
        {
            script.isAnalyzed = true;
            script.poseData = strposeDataPath;
        }
        else
        {
            script.isAnalyzed = true;
        }

        
        UnityEngine.Debug.Log("animate!");
    }
}
