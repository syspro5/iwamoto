using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using System;
using System.Diagnostics;
//

public class AnalyzeButton : MonoBehaviour
{

    string strBatFilePath;
    string strMovieFilePath;
    string strOpenposePath;
    string strLiftingPath;
    public InputField batFilePath;
    public InputField movieFilePath;
    public InputField OpenposePath;
    public InputField LiftingPath;

    public InputField InputField_outputPose3d;
    
    
    void Start()
    {
        strBatFilePath = Application.dataPath + @"/Resources/ExecuteAnalyzing.bat";//"@c:/users/%username%/desktop/extLib/ExecuteAnalyzing.bat";
        strOpenposePath = @"c:/users/%username%/desktop/extLib/openpose";//Application.dataPath + @"/Resources/openpose";
        strLiftingPath = @"c:/users/%username%/desktop/extLib/Lifting-from-the-Deep-release";//Application.dataPath + @"/Resources/Lifting";


    }

    public void whenPressed()
    {
        if (OpenposePath.text != "")
        {
            strOpenposePath = OpenposePath.text;
        }

        if (LiftingPath.text != "")
        {
            strLiftingPath = LiftingPath.text;
        }

        if (batFilePath.text != "")
        {
            strBatFilePath = batFilePath.text;
        }


        //strBatFilePath = batFilePath.text;
        strMovieFilePath = movieFilePath.text;

        Process p = new Process();
        p.StartInfo.FileName = strBatFilePath;
        p.StartInfo.Arguments = strMovieFilePath+" "+ strOpenposePath + " " + strLiftingPath;
        p.Start();
        UnityEngine.Debug.Log("EXecuting");

        p.WaitForExit();
        string rt = p.ExitCode.ToString();

        InputField_outputPose3d.text = rt;


    }
}