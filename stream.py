import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(3)

background = 0
 
for i in range(30):
    ret,background = cap.read()
    
while(cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break
    hsv=cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    