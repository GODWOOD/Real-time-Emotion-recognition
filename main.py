import record_video as RV

import time 
import tkinter as tk
from PIL import ImageTk , Image
import os
import cv2


class InterFace() :
    def __init__(self):
        #------variable----- 
        self.w_resultbox = 400      #GIF顯示視窗的大小
        self.h_resultbox = 300  

        self.StopRecord=[False]     #暫停錄影([BOOL]) 使用List來實現pass by refereance 
        self.GIFResultImage = None  #接收Pil.Image 調整大小後轉為tk.photoImage顯示在canvas
        self.FrameList=[]           #儲存GIF  [pil.Image*N]
        self.GIFStop=False          #開始錄影後 停止顯示GIF

        #-----------create GUI---------
        self.face=tk.Tk()
        self.face.title("Emotion Record")
        self.face.geometry('1100x550+0+0')
        self.face.configure(bg='white')

        #-------label+entry(row=0)-----------
        self.LabelFactory()
        self.CanvasFactory()
        self.PanelFactory()
        self.ButtonFactory()
        #----run GUI---------
        self.face.mainloop()

    def Buttom_Disable(self) : # 讓按鈕無法使用
        self.button_RecordVideo['state'] = 'disable' 
        self.button_restart['state'] = 'disable' 
        
    def Buttom_Recover(self) : # 恢復按紐
        self.button_RecordVideo['state'] = 'normal' 
        self.button_restart['state'] = 'normal' 

    def clickRecord(self) : # 開始錄影按鈕
        self.Buttom_Disable()
        self.StopRecord[0]=False
        self.GIFStop=True
        try :
            self.FrameList=RV.recordVideo("",self.panel,self.PredictEmotionSwitch.get(),self.GIFName.get(),self.StopRecord,self.RecordTime.get(),self.FaceRecognition.get())
            self.Buttom_Recover()
        except  Exception as e :
            print(e)
        finally :
            self.Buttom_Recover()
            self.GIFFrameCounter=len(self.FrameList)
            self.GIFIndex=0
            if self.GIFReverse.get() :
                self.FrameList.reverse()
            self.GIFStop=False
            self.showGIF()
    def clickStopRecord(self) :
        self.StopRecord[0]=True
    def showGIF(self) :
        if not self.GIFStop :
            self.GIFResultImage=self.FrameList[self.GIFIndex]
            self.GIFResultImage=self.resize(self.w_resultbox, self.h_resultbox, self.GIFResultImage)
            self.GIFResultImage=ImageTk.PhotoImage(self.GIFResultImage)
            self.canvas_ResultImage.delete('all')
            self.canvas_ResultImage.create_image(200, 0, anchor='n',image=self.GIFResultImage)
            self.GIFIndex+=1
            self.GIFIndex%=self.GIFFrameCounter
            self.face.after(100, self.showGIF)
    


    def clickSave(self) : # 存檔按鈕
        S=self.GIFName.get()
        if len(S)==0 :
            S=time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
            S=S+".gif"
        elif len(S)>3 :
            if not (S[-4]=="." and S[-3]=="g" and S[-2]=="i" and S[-1]=="f") :
                S=S+".gif"
        else :
            S=S+".gif"
        print(S)
        self.GIFName.set(S)
        if not os.path.isdir("GIF"):
            os.mkdir("GIF")
        self.FrameList[0].save("GIF\\"+self.GIFName.get(), save_all=True,loop=0 , append_images=self.FrameList, duration=100)
            
    def resize(self, w_box, h_box, pil_image): #修改Pil.Image圖片大小
        w, h = pil_image.size #取得pil.Image長寬
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h    
        factor = min([f1, f2])   
        width = int(w*factor)    
        height = int(h*factor)   
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def ButtonFactory(self) : # 建立按鈕
        self.button_RecordVideo=tk.Button(self.face,text="StartRecord",command=self.clickRecord,bg='#%02x%02x%02x' % (243, 252, 167),fg = "black")
        self.button_RecordVideo.place(x=280,y=500)


        self.button_StopRecordVideo=tk.Button(self.face,text="StopRecord",command=self.clickStopRecord,bg='#%02x%02x%02x' % (243, 252, 167),fg = "black")
        self.button_StopRecordVideo.place(x=360,y=500)


        self.button_restart=tk.Button(self.face,text="Save",command=self.clickSave,bg='#%02x%02x%02x' % (243, 252, 167),fg = "black")
        self.button_restart.place(x=1000,y=500)

    def LabelFactory(self) :
        LabelText=["Time : ","Emotion Predict : ","Face recognition : ","Reverse : "]
        self.OptionPosition_X=675                   #選項區的左上角X位置
        self.OptionPosition_Y=350                   #選項區的左上角Y位置
        self.RecordTime             = tk.IntVar()   #錄影時間
        self.PredictEmotionSwitch   =tk.BooleanVar()#啟用表情辨識
        self.FaceRecognition        =tk.BooleanVar()#啟用人臉偵測
        self.GIFReverse             =tk.BooleanVar()#啟用反轉
        self.GIFName                =tk.StringVar() #GIF存檔名稱
        
        for i,text in enumerate(LabelText) :
            tk.Label(self.face, text=text, width=15).place(x=self.OptionPosition_X,y=self.OptionPosition_Y+(i*25))
        tk.Label(self.face, text="GIF Name", width=10).place(x=700,y=500)

        tk.Entry(self.face,textvariable=self.RecordTime,width=4).place(x=self.OptionPosition_X+120,y=self.OptionPosition_Y+(0*25))
        tk.Checkbutton(self.face, text='Emotion Predict', variable=self.PredictEmotionSwitch, onvalue=True, offvalue=False,command=self.checkFaceAndEmotion).place(x=self.OptionPosition_X+120,y=self.OptionPosition_Y+(1*25))
        tk.Checkbutton(self.face, text='Face recognition', variable=self.FaceRecognition, onvalue=True, offvalue=False,command=self.checkFaceAndEmotion).place(x=self.OptionPosition_X+120,y=self.OptionPosition_Y+(2*25))
        tk.Checkbutton(self.face, text='Reverse', variable=self.GIFReverse , onvalue=True, offvalue=False).place(x=self.OptionPosition_X+120,y=self.OptionPosition_Y+(3*25))
        tk.Entry(self.face,textvariable=self.GIFName,width=25).place(x=800,y=500)
    def checkFaceAndEmotion(self) :
        self.FaceRecognition.set(self.PredictEmotionSwitch.get() or self.FaceRecognition.get())

    def CanvasFactory(self) : # 建立canvas 
        self.canvas_videoBG = tk.Canvas(self.face, bg='red', height=480, width=640)
        self.canvas_videoBG.place(x=0,y=0)

        self.canvas_ResultImage = tk.Canvas(self.face, bg='black', height=self.h_resultbox, width=self.w_resultbox)
        self.canvas_ResultImage.place(x=650,y=0)

    def PanelFactory(self) : # 建立panel
        self.panel = tk.Label(self.face,bg='blue')
        self.panel.place(x=0,y=0)
        
if __name__=='__main__' : # 程式進入點
    I=InterFace()