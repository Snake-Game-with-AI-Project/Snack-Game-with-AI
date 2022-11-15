import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()
font=pygame.font.Font("arial.ttf",25)
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
        if self.food in self.snake:
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
            self.score+=1
            self.creat_food()
        else:
            self.snake.pop()

        self.draw()
        self.clock.tick(SPEED)
        return self.game_over,self.score
    def draw(self):
        pass
    def _move(self,direction):
        pass
    def _is_collision(self):
        pass

game=Snake()

while True:
    game.play_step()
    if game.game_over:#
        break

print(game.score )
pygame.quit()