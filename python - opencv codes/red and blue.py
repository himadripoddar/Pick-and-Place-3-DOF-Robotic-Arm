import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame=cap.read()
    blurred=cv2.GaussianBlur(frame,(5,5),0)
    ret,thresh=cv2.threshold(blurred,210,255,0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(thresh, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_red = np.array([0,100,100])
    upper_red = np.array([20,255,255])
    lower_blue = np.array([70,50,50])
    upper_blue = np.array([120,255,255])
    
    # Threshold the HSV image to get only blue colors
    maskb = cv2.inRange(hsv, lower_blue, upper_blue)
    maskr = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    resb = cv2.bitwise_and(frame,frame, mask= maskb)
    resr = cv2.bitwise_and(frame,frame, mask= maskr)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('resb',resb)
    cv2.imshow('resr',resr)
    k=cv2.waitKey(5) & 0xff
    if k==27:
        break
    
cv2.destroyAllWindows()

