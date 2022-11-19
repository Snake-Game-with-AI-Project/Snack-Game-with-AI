import pygame
import random
from enum import Enum
from collections import namedtuple
from pygame import mixer
import shelve
mixer.init()
mixer.music.load('sound/Coin.mp3') #
pygame.init()
font=pygame.font.SysFont("arial",25)
class Direction(Enum):
    RIGHT=1
    LEFT=2
    UP=3
    DOWN=4
size=20
SPEED=10
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)
GRAY  =(105,105,105)
Point = namedtuple('Point', 'x, y')

class Snake:
    def __init__(self,w=640,h=480):
        self.h=h
        self.w=w
        self.game_over=False
        self.display=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Snake")
        self.clock=pygame.time.Clock() 
        self.direction=Direction.RIGHT
        self.head=Point(self.w/2,self.h/2) 
        self.snake=[self.head,Point(self.head.x-size,self.head.y),Point(self.head.x-(2*size),self.head.y)]
        self.score=0
        self.food=None
        self.creat_food()
    def creat_food(self):
        x = random.randint(0, (self.w-size )//size )*size 
        y = random.randint(0, (self.h-size )//size )*size
        self.food=Point(x,y)
        if self.food in self.snake or (self.food.x ==0 or self.food.x ==620 or self.food.y ==0 or self.food.y==460 ) :
            self.creat_food()
        
    def play_step(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.direction=Direction.LEFT
                elif event.key==pygame.K_RIGHT:
                    self.direction=Direction.RIGHT
                elif event.key==pygame.K_UP:
                    self.direction=Direction.UP
                elif event.key==pygame.K_DOWN:
                    self.direction=Direction.DOWN

        self._move(self.direction)
        self.snake.insert(0,self.head)
        if self._is_collision():
            self.game_over=True
            return self.game_over,self.score
        if self.head==self.food:
            mixer.music.play() 
            self.score+=1
            self.creat_food()
        else:
            self.snake.pop()

        self.draw()
        self.clock.tick(SPEED)
        return self.game_over,self.score
    def draw(self):
        if not self.game_over:
            self.display.fill(BLACK)
            for point in self.snake:
                pygame.draw.rect(self.display,BLUE1,pygame.Rect(point.x,point.y,size,size))
                pygame.draw.rect(self.display,BLUE2,pygame.Rect(point.x+4,point.y+4,12,12))
            pygame.draw.rect(self.display,RED,pygame.Rect(self.food.x,self.food.y,size,size))
            for i in range(640):
                for j in range(480):
                    if i==0 or j==0:
                        pygame.draw.rect(self.display,GRAY,pygame.Rect(i,j,size,size))
                    if i==620 or j ==460:
                        pygame.draw.rect(self.display,GRAY,pygame.Rect(i,j,size,size))
            text=font.render(f"Score: {self.score}",True,WHITE)
            self.display.blit(text,[0,0])
            pygame.display.flip()
    def gameover(self):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            
            with open("score.text",'r') as f:
                score=f.read()
            
            if self.score>int(score):
                bestScore=self.score
                with open('score.text','w') as f :
                    f.write(str(self.score))
            
               

            self.display.fill(BLACK)
            text=font.render(f"Score: {self.score}",True,WHITE)
            self.display.blit(text,[self.w/2-60,self.h/2-50])
            text=font.render(f"Game Over",True,WHITE)
            self.display.blit(text,[self.w/2-60,self.h/2-80])
            text=font.render(f"Best Score: {bestScore}",True,RED)
            self.display.blit(text,[self.w/2-60,self.h/2-110]) 
            pygame.display.flip()
            pygame.time.delay(2000)
            self.score=0
            self.game_over=False



    def _move(self,direction):
        x=self.head.x
        y=self.head.y
        if direction==Direction.RIGHT:
            x+=size
        elif direction==Direction.LEFT:
            x-=size
        elif direction==Direction.UP:
            y-=size
        elif direction==Direction.DOWN:
            y+=size
        self.head=Point(x,y)
    def _is_collision(self):

        if self.head.x > self.w - size or self.head.x < 0 or self.head.y > self.h - size or self.head.y < 0:
            self.game_over=False
            self.display=pygame.display.set_mode((self.w,self.h))
            pygame.display.set_caption("Snake")
            self.clock=pygame.time.Clock() 
            self.direction=Direction.RIGHT
            self.head=Point(self.w/2,self.h/2) 
            self.snake=[self.head,Point(self.head.x-size,self.head.y),Point(self.head.x-(2*size),self.head.y)]
            self.food=None
            self.creat_food()
            return True
        if self.head in self.snake[1:]:
            self.game_over=False
            self.display=pygame.display.set_mode((self.w,self.h))
            pygame.display.set_caption("Snake")
            self.clock=pygame.time.Clock() 
            self.direction=Direction.RIGHT
            self.head=Point(self.w/2,self.h/2) 
            self.snake=[self.head,Point(self.head.x-size,self.head.y),Point(self.head.x-(2*size),self.head.y)]
            self.food=None
            self.creat_food()
            return True
        return False
game=Snake()

while True:
    if not game.game_over:
        game.play_step()
    else:
        game.gameover()



print(game.score )

pygame.quit()