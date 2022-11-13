import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import random
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=.8, maxHands=1)
while True:
    success, img =cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    if hands:
        lmList =hands[0]["lmList"]
        point=lmList[8][0:2]
        cv2.circle(img,point,20,(200,0,200),cv2.FILLED)
    cv2.imshow("Image",img)
    cv2.waitKey(1)