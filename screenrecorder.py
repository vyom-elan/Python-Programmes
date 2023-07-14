from win32api import GetSystemMetrics
import numpy as np                          #pip install these libraries
import cv2
import pyautogui
import time
h = GetSystemMetrics(1)                                  #height
w =  GetSystemMetrics(0)                                #width
dim=(w,h)                                            #Ddimension of the video
f=cv2.VideoWriter_fourcc(*"XVID")        #XVID supports all popular video formats
output=cv2.VideoWriter("trecording.mp4",f,30.0,dim)    #records video in 30 fps with name as trecording
st=time.time()                   #st=start time
d=10                            #d=duration
et=st+d                        #et = endtime
while True:
    image=pyautogui.screenshot()
    frame_1=np.array(image)
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time=time.time()
    if c_time>et:
        break
output.release()
print("Recording Complete. Check the destination folder")
