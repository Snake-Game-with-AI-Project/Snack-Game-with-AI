import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()
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
        
    def creat_food(self):
        pass
    def play_step(self):
        pass
    def draw(self):
        pass
    def _move(self,direction):
        pass
      
    def _is_collision(self):
        pass

game=Snake()

while True:
    game.play_step()
    if game.game_over:
        break

print(game.score )
pygame.quit()