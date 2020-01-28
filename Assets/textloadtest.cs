using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using System;



public class textloadtest : MonoBehaviour
{
    public InputField inputField;
    public Text text;
    string mainPath = null;
    string textAsset = null;
    string poseData;
    string tmpFixedUpdateLine;
    bool isRunning = false;
    // string textAsset = null;


    void Start()
    {
        //this.gameObject.AddComponent<NKTextMan>(); //記入したScriptがComponentとして登録されているGameObjectにNKTextManを追加(手動でも可)
        //NKTextMan textMan = GetComponent<NKTextMan>();
        poseData = Application.dataPath + @"/Resources/sample.csv";

        //string filePath = Application.dataPath + @"/Resources/sample.txt";
        //Debug.Log(filePath);
        //// textAsset = Resources.Load<TextAsset>("sample.txt");
        //string text = textMan.readText("/Resources/out.csv");
        ////var textAsset = AssetDatabase.LoadAssetAtPath<text>
        //Debug.Log(text);


        //string[] words = text.Split(',');

        //int itr = 0;

        //foreach (var word in words)
        //{
        //    Debug.Log(itr);
        //    float f;
        //    if (float.TryParse(word, out f))
        //    {
        //        Debug.Log(f);
        //    }
        //    else
        //    {
        //        Debug.Log("Not number");
        //    }
        //    itr = itr + 1;
        //}


        //inputField = inputField.GetComponent<InputField>();
        //// text = text.GetComponent<Text>();
        //using (var ss = new StreamReader(poseData))
        //{
        //    while (ss.Peek() > -1)
        //    {
        //        Debug.Log(ss.ReadLine());

        //    }
        //}
        
    }

    void Update()
    {
        Debug.Log(tmpFixedUpdateLine);
        StartCoroutine("coRoutine");
    }


    public void InputText()
    {
        //テキストにinputFieldの内容を反映
        text.text = inputField.text;

    }
    
    IEnumerator coRoutine()
    {
        if (isRunning)
            yield break;
        isRunning = true;
        
        using (var sr = new StreamReader(poseData))
        {
            while (sr.Peek() > -1)
            {
                tmpFixedUpdateLine = sr.ReadLine();
                yield return null;
            }
        }

        isRunning = false;
    }
}

