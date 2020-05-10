import numpy
import cv2
cam= cv2.VideoCapture(0)
s,im=cam.read()
cv2.imshow('cam',im)
k=cv2.waitKey(5) & 0xFF
if k==27:
 
  cv2.destroyAllWindows()
