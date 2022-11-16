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
    def __init__(self, pathFood):
        self.points= [] # all points of the snake
        self.lengths= [] # distance between each point
        self.currentLength= 0 # total length of the snake
        self.allowedLength= 150 # total allowed length
        self.previousHead= 0, 0 # previous head point
       
        self.imgFood= cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint= 0,0
        self.randomFoodLocation()
       
        self.score=0
        self.gameOver= False
    def randomFoodLocation(self):
        '''
        method randomFoodLocation that change the location of donut randomly
        '''
        pass


    def update(self, imgMain, currentHead):
        '''
        method update that have all method inside it 
        '''
        pass


    def length_reduction(self):
        '''
        method Length_reduction that check the length must be less than the allowed length
        '''
        pass


    def check_if_eaten(self):
        '''
        method check_if_eaten that check if snake is eat the food
        '''
        pass


    def draw_snake(self):
        '''
        method draw_snake that draw snake
        '''
        pass


    def draw_food(self):
        '''
        method draw_food that draw the donut
        '''
        pass


    def collision(self):
        '''
        method Collision that check if the snake hit itself

        '''
        pass

# game= SnakeGameClass("../assets/Donut.png")


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