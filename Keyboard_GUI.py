
import pygame
from Button_GUI import Button2 , Button3 , Button4
pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('Snake Game')


icon = pygame.image.load('assets\snake.png')
pygame.display.set_icon(icon)
# AI_img = pygame.image.load('assets\AI.png').convert_alpha()

Mouse_img = pygame.image.load('assets\Buttons.png').convert_alpha()
Back_img = pygame.image.load('assets\Back.png').convert_alpha()

# add text by pygame
font = pygame.font.Font('freesansbold.ttf',30,italic=True,bold=True)
text = font.render('How to play Snake Game by using Keyboard',True,(0,0,0))

class Button:
    
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image , (int(width * scale) , int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.clicked = False
    def draw(self):
        
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0]==0:
            self.clicked = False

        screen.blit(self.image , (self.rect.x , self.rect.y))
        return action

# AI_button = Button(299 ,300 , AI_img , 0.3)
Mouse_button = Button(299 , 360 , Mouse_img , 0.3)
Back_img = Button(4,15 ,Back_img,0.09)



clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)
button1 = Button2('Watch tutorial',200,40,(280,150),5)
button3 = Button3('Play The Game',200,40,(280,220),5)
button4 = Button4("Quit",200,40,(280,290),5)

run = True
while run:
    
    screen.fill((202 ,228 , 241))
    if Mouse_button.draw():
        print("AI button clicked")

    if Back_img.draw():
        print("Back")
    button1.draw()
    button3.draw()
    button4.draw()
    #if Mouse_button.draw():
        #print("Mouse Button clicked")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False
    

    screen.blit(text,(120,60))
    
    pygame.display.update()
    
  
pygame.quit()



    