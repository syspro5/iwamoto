using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System;
using System.Diagnostics;
//

public class aaa : MonoBehaviour
{
    // string scriptPath = Application.dataPath + "/StreamingAssets/ProcessScripts/";
    // Start is called before the first frame update
    void Start()
    {
        Process p = new Process();
        p.StartInfo.FileName = "C:/Users/IWMTT/Desktop/kesuna.bat";
        p.Start();
        UnityEngine.Debug.Log("aaaaa");

    }

    // Update is called once per frame
    void Update()
    {
        
    }

}
