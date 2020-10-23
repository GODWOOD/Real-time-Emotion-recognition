import tensorflow as tf
import os
import dlib
import cv2
import numpy as np
#['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

class Model() :
    def __init__(self):
        self.Model = tf.keras.models.load_model('Model_fer2013.h5')#讀取moudle
        self.Result=[]#儲存辨識結果

    def predict(self,Frame) :#進行預測
        Ans=self.Model.predict(self.Frame2Tensor(Frame))
        Ans=np.where(Ans==np.max(Ans))
        self.Result.append(Ans[1][0])
    def Frame2Tensor(self,Frame) :#將圖片轉為Tensor
        Frame=Frame*(1./255)
        Frame=np.array(Frame)
        Frame=tf.convert_to_tensor(Frame,dtype=tf.float32)
        return tf.reshape(Frame,[1,48,48,1])
    def getResult(self) :#返回辨識結果
        if len(self.Result)>0 :
            return self.Result.pop(0)
        else :
            return -1