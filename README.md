# Real-time-Emotion-recognition
    Emotion recognition in real-time and save mp4 and gif

## Environment
    W10
    Python : 3.6
    Tensorflow2.0
    Install "dlib" : First, visual studio and Cmake are necessary or it will have some errors.
    The emotion Model Download URL is in the txt file.
## 使用方法
    It is possible to choose using the face-dectection, emotion-prediction and reverse-timeline.
    (Using the emotion-prediction will also using the face-dectection)
    The time is able to type in. 0 means it won't end until press the StopButtom. 
    (P.S. You can end it early by pressing the StopButtom before the time is up.)
    press StartRecord to start recording.
    press StopRecord to end the recording.
    Type in the filename of GIF before press the Save buttom(Using the time right now as default.)
    (Every video will save in the "video" folder, the GIF will save only the Save buttom been pressed.)
## Model Introduction
    Using 48*48*1 with one signal picture
    training 500 times with 128 pictures as one time.
    Using FER2013 as data.
![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/AC_500_65.png)
![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/L_500_65.png)
## DEMO with GIF
![image](https://github.com/GODWOOD/Real-time-Emotion-recognition/blob/main/demo.gif)

