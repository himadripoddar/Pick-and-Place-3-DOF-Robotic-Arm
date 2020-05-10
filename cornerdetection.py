import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while(True):
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray,25,0.01,150)
    corners = np.int0(corners)
    for corner in corners :
        x,y = corner.ravel()
    
        cv2.circle (frame, (x,y), 3, 255, -1 )
    cv2.imshow('frame',frame)
    k=cv2.waitKey(5) & 0xff
    if k==27:
        break
cv2.destroyAlLWindows()
cap.release()
    
 
