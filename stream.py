import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(3)

background = 0
 
for i in range(30):
    ret,background = cap.read()
    