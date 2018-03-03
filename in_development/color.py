import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    _,image=cap.read()
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    s=25
    w=np.array([60-s,100,50])
    s=np.array([60+s,255,255])

    mask=cv2.inRange(hsv,w,s)

    cv2.imshow('Image',image)
    cv2.imshow('res',mask)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
cap.release
cv2.destroyAllWindows()
