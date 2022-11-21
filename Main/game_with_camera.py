import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math,os
import random
import pygame


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=.8, maxHands=1)


class SnakeGameClass:
    pathFood=['assets\mais.png','assets/rania.png','assets\islam.png','assets\mohammad.png']
    
    def __init__(self):
        self.points= [] # all points of the snake
        self.lengths= [] # distance between each point
        self.currentLength= 0 # total length of the snake
        self.allowedLength= 250 # total allowed length
        self.previousHead= 0, 0 # previous head point
        self.score=0
        self.best_score=0
        self.msg=''
        self.user_name=''
        self.best_user=''
        self.rand=random.randint(0, len(SnakeGameClass.pathFood)-1)
        self.user_best_score=0
        self.gameOver= False    
        self.imgFood= cv2.imread(SnakeGameClass.pathFood[self.rand], cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint= 0,0
        self.randomFoodLocation()
    def Collision(self,imgMain,currentHead):
            cx, cy= currentHead
            pts= np.array(self.points[:-2],np.int32)
            pts= pts.reshape((-1,1,2))
            cv2.polylines(imgMain,[pts],False,(0,200,0),3)
            minDis= cv2.pointPolygonTest(pts,(cx,cy),True)
           
            if -1 <= minDis <=1 or cx<=10 or cx>=1270 or cy<=10 or cy>=690:
                pygame.mixer.music.load("assets\game_over_sound.wav")
                pygame.mixer.music.play()
                print("Hit")
                self.gameOver=True
            
                try:       
                    with open("Score/AI_score",'r') as file:
                        recorded_score= file.read()
                        # print(recorded_score)
                    if self.score>int(recorded_score):
                        self.best_score=self.score
                        self.msg='Good job'
                        with open('Score/AI_score', 'w') as file:
                            file.write(self.score)
                    else:
                        self.best_score=recorded_score
                        self.msg='Try again'
                        
                except:
                    self.best_score=self.score
                    self.msg='Good job'
                    path=os.path.join('Score','AI_score')
                    with open(path, 'w') as file:
                        file.write(str(self.best_score))
                        
                list_of_files = os.listdir("./Main/users")
                dic={}
                for i,us in enumerate(list_of_files):
                    path2=os.path.join('Main/users',list_of_files[i])
                    with open(path2,'r') as f:
                        x= f.read().splitlines()[2]
                        dic[us]=int(x)
                # print(dic)
                        
                maxx=0
                for key,score in dic.items():
                    if score> maxx:
                        maxx= score
                        self.best_user=key
                
                with open('user_name','r') as file:
                    self.user_name= file.read()
                path1=os.path.join('Main/users',self.user_name)
                
                with open(path1,'r') as file1:
                    list_content=file1.read().splitlines()
                    try:
                        prev_score= list_content[2]
                    except:
                        prev_score=0
                        
                with open(path1,'w') as file:
                    for s in list_content[:2]:
                        file.write(s + "\n")
                    if self.score> int(prev_score):
                        self.user_best_score=self.score
                    else:
                        self.user_best_score=int(prev_score)
                    file.write(str(self.user_best_score))
                    
                
                        
                
                
                
                self.points= [] # all points of the snake
                self.lengths= [] # distance between each point
                self.currentLength= 0 # total length of the snake
                self.allowedLength= 150 # total allowed length
                self.previousHead= 0, 0 # previous head point
                self.randomFoodLocation()
       

    def randomFoodLocation(self):
        self.foodPoint= random.randint(100,1000),random.randint(100,600)
        self.rand=random.randint(0,len(SnakeGameClass.pathFood)-1)
        self.imgFood= cv2.imread(SnakeGameClass.pathFood[self.rand], cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape

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
            pygame.mixer.music.load("assets\eat_sound.wav")
            pygame.mixer.music.play()
            self.randomFoodLocation()
            self.allowedLength +=50
            self.score +=1
    def draw_snake(self,imgMain):
            '''
            method draw_snake that draw snake
            '''
            with open('user_name','r') as file:
                self.user_name= file.read()
                
            with open("Score/AI_score",'r') as file:
                recorded_score= file.read()
                # print(recorded_score)
               
            list_of_files = os.listdir("./Main/users")
            dic={}
            for i,us in enumerate(list_of_files):
                path2=os.path.join('Main/users',list_of_files[i])
                with open(path2,'r') as f:
                    l= f.read().splitlines()
                    
                    if len(l)==3:
                        x= l[2]
                        dic[us]=int(x)
                    else:
                        dic[us]=0
                        l.append('0')
                        with open(path2,'w') as f:
                            for i in l:
                                f.write(i+'\n')
          
            maxx=0
            for key,score in dic.items():
                if score> maxx:
                    maxx= score
                    self.best_user=key
                    
                    
            if self.points:
                for i,point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i-1],self.points[i],(255,255,0),20)
                cv2.circle(img,self.points[-1],20,(255,255,0),cv2.FILLED)

            cvzone.putTextRect(imgMain, f'Score: {self.score}', [50,80],scale=3,thickness=3,offset=10)
            cvzone.putTextRect(imgMain, f'{self.user_name}', [400,80],scale=3,thickness=3,offset=10)
            cvzone.putTextRect(imgMain, f'1st {self.best_user}: {recorded_score}', [750,80],scale=3,thickness=3,offset=10)
    def update(self,imgMain,currentHead):
        '''
        method update that have all method inside it 
        '''
        if self.gameOver:
            cvzone.putTextRect(imgMain, f"Name: {self.user_name}",[80,150],scale=4,thickness=5,offset=20)
            cvzone.putTextRect(imgMain, f'Your score: {self.score}', [80,250],scale=4,thickness=5,offset=20)
            cvzone.putTextRect(imgMain, f'Your highest score: {self.user_best_score}', [80,350],scale=4,thickness=5,offset=20)
            cvzone.putTextRect(imgMain, self.msg, [80,450],scale=5,thickness=5,offset=20)
            # cvzone.putTextRect(imgMain, "Game Over",[80,650],scale=4,thickness=5,offset=20)
        else:
            cv2.line(imgMain, [0,0],[1280,0],(0,0,255),20)
            cv2.line(imgMain, [0,700],[1280,700],(0,0,255),20)
            cv2.line(imgMain, [0,0],[0,700],(0,0,255),20)
            cv2.line(imgMain, [1280,0],[1280,700],(0,0,255),20)
            px, py= self.previousHead
            cx, cy= currentHead

            self.points.append([cx,cy])
            distance= math.hypot(cx-px,cy-py)
            self.lengths.append(distance)
            self.currentLength +=distance
            self.previousHead= cx, cy
            self.reduction()
            self.check_eaten(currentHead)
            self.draw_snake(imgMain)
            rx, ry = self.foodPoint
            # print(rx - self.wFood//2)
            imgMain= cvzone.overlayPNG(imgMain, self.imgFood,(rx - self.wFood//2 , ry - self.hFood//2))
            self.Collision(imgMain,currentHead)
        return imgMain
game= SnakeGameClass()
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