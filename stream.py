import numpy as np
import cv2
import time
import win10toast
import pyttsx3

speak=pyttsx3.init()

notifi = win10toast.ToastNotifier()
notifi.show_toast("Invisible_cloak","Hey Manish your program has started",duration=3)

speak.say("hello Maneesh Welcome your video is going to be captured soon sirr")
speak.runAndWait()

cap = cv2.VideoCapture(0)
# address="https://192.168.1.3:8080/cap"
# cap.open(address)


time.sleep(2)

background = 0

speak.say("here is it in your service ")
speak.runAndWait()


for i in range(30):
    ret,background = cap.read()
    

while(cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break
    hsv=cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 120 , 70])
    upper_red = np.array([0, 255 , 255])

    mask1=cv2.inRange(hsv,lower_red,upper_red)
    
    lower_red = np.array([170, 120 , 70])
    upper_red = np.array([180, 255 , 255])

    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1 ,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.morphologyEx(mask1 ,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(img, img, mask = mask2) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 

    cv2.imshow("Invisible Manish !", final_output) 
    k = cv2.waitKey(10) 
    if k == 27: 
        break
    
speak.say("Thankyou for your visit,have a good day sir")
speak.runAndWait()

cap.release()
cv2.destroyAllWindows()

