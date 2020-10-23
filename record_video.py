import cv2
import time
import os
from PIL import Image,ImageTk
import dlib
import Emotion_Predict as EP

TFModel=EP.Model()
Emotion=['Angry', 'Digust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Natural']

def recordVideo(Video_Path,panel,PredictEmotionSwitch,Recorder_Name,StopRecord,RecordTime,FaceRecognition):
    FrameList=[] #GIF圖片List ([pil.Image])
    if Recorder_Name==None :
        Recorder_Name=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(Recorder_Name)

    try :#錄影時間
        Record_Time=int(RecordTime)
    except :
        Record_Time=0         
                  
    Face68Point=False
    Video_Path="video"+"\\"+Video_Path#影片存檔路徑
    if not os.path.isdir(Video_Path):
        os.mkdir(Video_Path)
    Video_Path=Video_Path+"\\"+Recorder_Name+".mp4"

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #開啟攝影機

    #影像長寬 偵數 設定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    #print(sz)
    fps = 30
    # 輸出格式
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    vout = cv2.VideoWriter()
    vout.open(Video_Path, fourcc, fps, sz, True)

    T0=time.time()


    detector = dlib.get_frontal_face_detector()    #Dlib的人臉偵測
    
    if Face68Point :#68點人臉特徵
        predictor = dlib.shape_predictor( 'shape_predictor_68_face_landmarks.dat')

    while True:
        _, frame = cap.read()
        #文字輸出到視訊上，參數依序是：圖片/新增的文字/左上角座標/字型/字型大小/顏色/字型粗細
        cv2.putText(frame, str(int(time.time()-T0)), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
        vout.write(frame)

        # 偵測人臉
        face_rects, scores, idx = detector.run(frame, 0)
        # 取出所有偵測的結果
        Frame=frame
        for i, d in enumerate(face_rects):
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()

            #標出偵測到的人臉
            if FaceRecognition :
                cv2.rectangle(frame, (x1-30, y1-30), (x2+30, y2+30), (0, 255, 0), 4, cv2.LINE_AA)
            Frame=frame[max(y1-30,0):min(y2+30,480),max(x1-30,0):min(x2+30,640)]
            if face_rects :
                pass

            """# 標示分數
            cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
                    0.7, (255, 255, 255), 1, cv2.LINE_AA)"""
            if Face68Point :
                #給68特徵點辨識取得一個轉換顏色的frame
                landmarks_frame = cv2.cvtColor(frame, cv2. COLOR_BGR2RGB)

                #找出特徵點位置
                shape = predictor(landmarks_frame, d)
            
                #畫出68個特徵點
                for i in range( 68):
                    cv2.circle(frame,(shape.part(i).x+200,shape.part(i).y), 3,( 0, 0, 255), 1)
    
            if PredictEmotionSwitch : #表情辨識
                Frame=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
                Frame=cv2.resize(Frame,(48,48))
                TFModel.predict(Frame)
                Result=TFModel.getResult()
                cv2.putText(frame, Emotion[Result], (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)

        
        FrameList.append(Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)))

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)#轉換顏色 BGR->RGBA
        current_image = Image.fromarray(cv2image)#轉為pil.Image
        imgtk = ImageTk.PhotoImage(image=current_image)#轉為tk.PhotoImage
        
        panel.imgtk = imgtk#顯示拍攝到的影像圖片
        panel.config(image=imgtk)
        panel.update()
        #結束錄影
        if (cv2.waitKey(1) & 0xFF == ord('q')) or (time.time()-T0>=Record_Time and Record_Time>0) or StopRecord[0]:
            break
    print("Frame",len(FrameList))
    vout.release()
    cap.release() 
    return FrameList