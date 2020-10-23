# Real-time-Emotion-recognition
    Emotion recognition in real-time and save mp4 and gif
    原本只有表情辨識 覺得太單調 就把GIF也加進去
## 環境
    W10
    Python : 3.6
    Tensorflow2.0
    安裝dlib : 需要先安裝visual studio 以及 Cmake  直接pip install dlib會出錯
    要去txt當中的雲端下載表情辨識的model(超過25MB不給傳)
## 使用方法
    打開後
    可選擇是否使用人臉偵測 表情辨識 以及時間軸反轉(開啟表情辨識同時會開啟人臉偵測)
    按StartRecord開始錄影
    按StartRecord開始錄影
## Model介紹
    輸入為48*48*1的單通道黑白圖片
    訓練次數500次每次128張
    使用fer2013
    ![](https://drive.google.com/file/d/1Cc_PiWp9bkvaIc6bS130jkSwMsHMBiNi/view?usp=sharing)
    ![](https://drive.google.com/file/d/1I7ytFZZs4pflQoYRVgoXYH8vDiVWwGGn/view?usp=sharing)
