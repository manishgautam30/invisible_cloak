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
    
    lower_red = np.array([0, 120 , 70])
    upper_red = np.array([0, 255 , 255])

    mask1=cv2.inRange(hsv.lower_red,upper_red)
    
    lower_red = np.array([170, 120 , 70])
    upper_red = np.array([180, 255 , 255])

    mask2=cv2.inRange(hsv.lower_red,upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1 ,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.morphologyEx(mask1 ,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)
    