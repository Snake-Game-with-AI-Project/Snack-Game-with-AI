import pygame
from button_images import *

# Button class
class Button:
    def __init__(self,x,y,image,scale):
        self.screen=pygame.display.set_mode((800,600))
        width= image.get_width()
        height= image.get_height()
        self.image= pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect= self.image.get_rect() # to get a rectangle from it
        self.rect.topleft=(x,y)
        self.clicked= False

    def draw(self):
        action= False
        # get mouse position
        pos= pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # index0:left mouse btn | index1:middle mouse btn | index2: right mouse btn
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        # draw btn on screen
        self.screen.blit(self.image, (self.rect.x,self.rect.y))
        return action
    
# create buttons
option1_btn=Button(300,230,option1_img,0.7)
option2_btn=Button(300,330,option2_img,0.7)
exit_btn= Button(300,430,exit_img,0.7)
mute_btn= Button(720,530,mute_img,1)
low_volume_btn= Button(650,530,low_volume_img,1)
high_volume_btn= Button(580,530,high_volume_img,1)