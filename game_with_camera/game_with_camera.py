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


class SnakeGameClass:
    def __init__(self):
        self.points= [] # all points of the snake
        self.lengths= [] # distance between each point
        self.currentLength= 0 # total length of the snake
        self.allowedLength= 250 # total allowed length
        self.previousHead= 0, 0 # previous head point

    def update(self,imgMain,currentHead):
        '''
        method update that have all method inside it 
        '''
        px, py= self.previousHead
        cx, cy= currentHead

        self.points.append([cx,cy])
        distance= math.hypot(cx-px,cy-py)
        self.lengths.append(distance)
        self.currentLength +=distance
        self.previousHead= cx, cy
        

        # Length reduction
        def reduction():
            '''
            method Length_reduction that check the length must be less than the allowed length
            '''
            if self.currentLength >self.allowedLength:
                for i,length in enumerate(self.lengths):
                    self.currentLength -=length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

        # Draw snake
        def draw_snake():
            '''
            method draw_snake that draw snake
            '''
            if self.points:
                for i,point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i-1],self.points[i],(0,0,255),20)
                cv2.circle(img,self.points[-1],20,(200,0,200),cv2.FILLED)
        reduction()
        draw_snake()
        return imgMain

game= SnakeGameClass()


while True:
    success, img =cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    if hands:
        lmList =hands[0]["lmList"]
        pointIndex=lmList[8][0:2]
        game.update(img,pointIndex)
    cv2.imshow("Image",img)
    cv2.waitKey(1)