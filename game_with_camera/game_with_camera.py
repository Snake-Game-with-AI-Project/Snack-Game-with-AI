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
    def __init__(self,pathFood):
        self.points= [] # all points of the snake
        self.lengths= [] # distance between each point
        self.currentLength= 0 # total length of the snake
        self.allowedLength= 250 # total allowed length
        self.previousHead= 0, 0 # previous head point

        self.imgFood= cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint= 0,0
        self.randomFoodLocation()


    def randomFoodLocation(self):
        self.foodPoint= random.randint(100,1000),random.randint(100,600)

    def reduction(self):
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
    def check_eaten(self,currentHead):
        cx, cy= currentHead
        rx, ry = self.foodPoint
        if rx- self.wFood//2 < cx < rx + self.wFood//2 and ry -self.hFood // 2< cy<ry+self.hFood//2:
            self.randomFoodLocation()
            self.allowedLength +=50
            self.score +=1
            print(self.score)
    def draw_snake(self,imgMain):
            '''
            method draw_snake that draw snake
            '''
            if self.points:
                for i,point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i-1],self.points[i],(0,0,255),20)
                cv2.circle(img,self.points[-1],20,(200,0,200),cv2.FILLED)

            cvzone.putTextRect(imgMain, f'Score: {self.score}', [50,80],scale=3,thickness=3,offset=10)
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
        self.score=0
        self.gameOver= False
        self.reduction()
        self.check_eaten(currentHead)
        self.draw_snake(imgMain)
        rx, ry = self.foodPoint
        print(rx - self.wFood//2)
        imgMain= cvzone.overlayPNG(imgMain, self.imgFood,(rx - self.wFood//2 , ry - self.hFood//2))
        return imgMain

game= SnakeGameClass("assets\Donut.png")
while True:
    success, img= cap.read()
    img= cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)
   
    if hands:
        lmList= hands[0]['lmList']
        pointIndex= lmList[8][0:2]
        img= game.update(img,pointIndex)
       
    cv2.imshow("Image", img)
    key= cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver= False
        game.score=0
    if key== ord('q'):
        break