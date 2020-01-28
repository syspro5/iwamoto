using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using System;



public class csv2pose : MonoBehaviour
{
    public string poseData;
    string tmpFixedUpdateLine="hoge";
    bool isRunning = false;
    float LenSpine2uL;
    float LenUL2knee;
    float LenKnee2foot;
    float LenSpine2shoulder;
    float LenShoulder2elbow;
    float LenElbow2hand;


    public GameObject spine;
    public GameObject head;
    public GameObject footR;
    public GameObject footL;
    public GameObject handR;
    public GameObject handL;

    public GameObject elbowR;
    public GameObject elbowL;
    public GameObject kneeR;
    public GameObject kneeL;

    public GameObject shoulderR;
    public GameObject shoulderL;
    public GameObject uLegR;
    public GameObject uLegL;

    public GameObject model_spine;
    public GameObject model_head;
    public GameObject model_footR;
    public GameObject model_handR;
    
    public GameObject model_elbowR;
    public GameObject model_kneeR;
    
    public GameObject model_shoulderR;
    public GameObject model_uLegR;

    public float Yoffset = 1.0f;

    public bool isAnalyzed = false;


    void Start()
    {

        poseData = Application.dataPath + @"/Resources/NormPose3ds.csv";
        //string filePath = Application.dataPath + @"/Resources/sample.txt";

        //get model's bone length
        Vector3 model_Spine2uL = model_uLegR.transform.position - model_spine.transform.position;
        Vector3 model_uL2knee = model_kneeR.transform.position - model_uLegR.transform.position;
        Vector3 model_knee2foot = model_footR.transform.position - model_kneeR.transform.position;
        Vector3 model_Spine2shoulder = model_shoulderR.transform.position - model_spine.transform.position;
        Vector3 model_shoulder2elbow = model_elbowR.transform.position - model_shoulderR.transform.position;
        Vector3 model_elbow2hand = model_handR.transform.position - model_elbowR.transform.position;
        LenSpine2uL = model_Spine2uL.magnitude;
        LenUL2knee = model_uL2knee.magnitude;
        LenKnee2foot = model_knee2foot.magnitude;
        LenSpine2shoulder = model_Spine2shoulder.magnitude;
        LenShoulder2elbow = model_shoulder2elbow.magnitude;
        LenElbow2hand = model_elbow2hand.magnitude;
    }

    void FixedUpdate()
    {
        if (isAnalyzed)
        {
            StartCoroutine("coRoutine");
            //Debug.Log(tmpFixedUpdateLine);
            string[] stArrayData = tmpFixedUpdateLine.Split(',');

            //spine
            Vector3 posspine = new Vector3(float.Parse(stArrayData[0]), float.Parse(stArrayData[17]) + Yoffset, float.Parse(stArrayData[34]));
            spine.transform.position = posspine;

            //vectors
            Vector3 spine2chest = new Vector3(float.Parse(stArrayData[8]), float.Parse(stArrayData[25]), float.Parse(stArrayData[42]));
            Vector3 chest2chin = new Vector3(float.Parse(stArrayData[9]), float.Parse(stArrayData[26]), float.Parse(stArrayData[43]));
            Vector3 chin2chest = new Vector3(float.Parse(stArrayData[10]), float.Parse(stArrayData[27]), float.Parse(stArrayData[44]));
            Vector3 spine2hips = new Vector3(float.Parse(stArrayData[7]), float.Parse(stArrayData[24]), float.Parse(stArrayData[41]));
            Vector3 hips2uLR = new Vector3(float.Parse(stArrayData[1]), float.Parse(stArrayData[18]), float.Parse(stArrayData[35]));
            Vector3 hips2uLL = new Vector3(float.Parse(stArrayData[4]), float.Parse(stArrayData[21]), float.Parse(stArrayData[38]));
            Vector3 uL2kneeR = new Vector3(float.Parse(stArrayData[2]), float.Parse(stArrayData[19]), float.Parse(stArrayData[36]));
            Vector3 uL2kneeL = new Vector3(float.Parse(stArrayData[5]), float.Parse(stArrayData[22]), float.Parse(stArrayData[39]));
            Vector3 knee2footR = new Vector3(float.Parse(stArrayData[3]), float.Parse(stArrayData[20]), float.Parse(stArrayData[37]));
            Vector3 knee2footL = new Vector3(float.Parse(stArrayData[6]), float.Parse(stArrayData[23]), float.Parse(stArrayData[40]));
            Vector3 chest2shoulderR = new Vector3(float.Parse(stArrayData[14]), float.Parse(stArrayData[31]), float.Parse(stArrayData[48]));
            Vector3 chest2shoulderL = new Vector3(float.Parse(stArrayData[11]), float.Parse(stArrayData[28]), float.Parse(stArrayData[45]));
            Vector3 shoulder2elbowR = new Vector3(float.Parse(stArrayData[15]), float.Parse(stArrayData[32]), float.Parse(stArrayData[49]));
            Vector3 shoulder2elbowL = new Vector3(float.Parse(stArrayData[12]), float.Parse(stArrayData[29]), float.Parse(stArrayData[46]));
            Vector3 elbow2handR = new Vector3(float.Parse(stArrayData[16]), float.Parse(stArrayData[33]), float.Parse(stArrayData[50]));
            Vector3 elbow2handL = new Vector3(float.Parse(stArrayData[13]), float.Parse(stArrayData[30]), float.Parse(stArrayData[47]));



            //uLeg
            uLegR.transform.position = (hips2uLR + spine2hips) / (hips2uLR + spine2hips).magnitude * LenSpine2uL + posspine;
            uLegL.transform.position = (hips2uLL + spine2hips) / (hips2uLL + spine2hips).magnitude * LenSpine2uL + posspine;

            //knee
            kneeR.transform.position = uL2kneeR * LenUL2knee + uLegR.transform.position;
            kneeL.transform.position = uL2kneeL * LenUL2knee + uLegL.transform.position;

            //foot
            footR.transform.position = knee2footR * LenKnee2foot + kneeR.transform.position;
            footL.transform.position = knee2footL * LenKnee2foot + kneeL.transform.position;

            //shoulder
            shoulderR.transform.position = posspine + (spine2chest + chest2shoulderR) * LenSpine2shoulder;
            shoulderL.transform.position = posspine + (spine2chest + chest2shoulderL) * LenSpine2shoulder;

            //elbow
            elbowR.transform.position = shoulderR.transform.position + shoulder2elbowR * LenShoulder2elbow;
            elbowL.transform.position = shoulderL.transform.position + shoulder2elbowL * LenShoulder2elbow;

            //hand
            handR.transform.position = elbowR.transform.position + elbow2handR * LenElbow2hand;
            handL.transform.position = elbowL.transform.position + elbow2handL * LenElbow2hand;

            //chin
            head.transform.position = posspine + spine2chest + chest2chin + chin2chest;
        }
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

