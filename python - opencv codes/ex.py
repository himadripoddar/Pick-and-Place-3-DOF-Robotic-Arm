import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while(True):
    _,frame=cap.read()
    print frame.shape
    cv2.imshow('frame',frame)
    k=cv2.waitKey(5)
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
