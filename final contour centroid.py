import numpy as np
import cv2
import serial
import time

ArduinoSerial = serial.Serial('com17',9600)
time.sleep(2)
cam = cv2.VideoCapture(0)

s,frame=cam.read()
gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
ret,thresh=cv2.threshold(blurred,120,255,0)
   
    
_,contours,_= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
     
#cnt = contours[0]
for c in contours:
    M=cv2.moments(c)
    cx= int(M["m10"]/ M["m00"])
    cy= int(M["m01"]/ M["m00"])
    cv2.drawContours(frame, [c], -1, (255,0,0), 3)
    cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
    print cx
    print cy
    go=['cx','cy']
    ArduinoSerial.write(go)
    
    time.sleep(1)
        
    
cv2.imshow('img',frame)
cv2.imshow('thresh',thresh)
k=cv2.waitKey(0)

    
cv2.destroyAllWindows()

    
