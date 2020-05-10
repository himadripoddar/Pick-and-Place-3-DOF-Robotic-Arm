import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    _,frame=cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh=cv2.threshold(blurred,100    ,255,0)
   
    
    contours= cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    ##img = cv2.drawContours(frame, contours, -1, (255,0,0), 3)
    cnt=contours[0]
    M=cv2.moments(cnt)
    cx= int(M["m10"]/ M["m00"])
    cy= int(M["m01"]/ M["m00"])
    cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
    
    cv2.imshow('img',img)
    cv2.imshow('thresh',thresh)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
    
