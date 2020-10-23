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
    輸入GIF的檔案名稱後按Save存檔(沒有輸入檔名會用當前時間為檔名儲存)
    (拍攝的所有影片都會存入video資料夾 GIF則是按存檔才會儲存)
## Model介紹
    輸入為48*48*1的單通道黑白圖片
    訓練次數500次每次128張
    使用fer2013 改天有空再把訓練model的程式放上來
    ![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/AC_500_65.png)
    ![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/L_500_65.png)
## DEMO
    ![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/demo.gif)

