import cv2
import numpy as np
cam = cv2.VideoCapture(0)

# Take each frame
_, frame=cam.read()
blurred=cv2.GaussianBlur(frame,(5,5),0)
ret,thresh=cv2.threshold(blurred,50,255,0)
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

mask_invb=cv2.bitwise_not(resb)
mask_invr=cv2.bitwise_not(resr)
grayb= cv2.cvtColor(mask_invb,cv2.COLOR_BGR2GRAY)
grayr= cv2.cvtColor(mask_invr,cv2.COLOR_BGR2GRAY)
#blurred1=cv2.GaussianBlur(gray,(5,5),0)
#ret,thresh1=cv2.threshold(blurred1,50,255,0)
finalb=cv2.bitwise_not(grayb)
finalr=cv2.bitwise_not(grayr)
_,contoursb,_= cv2.findContours(finalb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for b in contoursb:
    M=cv2.moments(b)
    cxb= int(M["m10"]/ M["m00"])
    cyb= int(M["m01"]/ M["m00"])
    cv2.drawContours(frame, [b], -1, (0,255,0), 3)
    cv2.circle(frame,(cxb,cyb),5,(0,255,0),-1)
    print("for blue")
    print cxb
    print cyb
    break
_,contoursr,_= cv2.findContours(finalr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for r in contoursr:
    R=cv2.moments(r)
    cxr= int(R["m10"]/ R["m00"])
    cyr= int(R["m01"]/ R["m00"])
    cv2.drawContours(frame, [r], -1, (0,255,0), 3)
    cv2.circle(frame,(cxr,cyr),5,(0,255,0),-1)
    print ("for red")
    print cxr
    print cyr
    break
cv2.imshow('frame',frame)
#cv2.imshow('mask',mask_inv)
#cv2.imshow('resb',finalb)
#cv2.imshow('resr',finlr)
k=cv2.waitKey(0)

    
cv2.destroyAllWindows()

