import cv2
import time
from cv2 import resize
import numpy as np

Video=cv2.VideoCapture(0)
image=cv2.imread('minion.jpeg')

while True:
    ret,frame=Video.read()
    print(frame)
    frame=cv2.resize(frame,(640,400))
    image=cv2.resize(frame,(640,400))
    upper_black=np.array([104,153,70])
    lower_black=np.array([30,30,0])
    mask=cv2.inRange(frame,lower_black,upper_black)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-res
    f=np.where(f==0,image,f)
    cv2.imshow('Video',frame)
    cv2.imshow('mask',f)

    if cv2.waitKey(1)&0xFF==ord('q'):
         break
Video.release()
cv2.destroyAllWindows()