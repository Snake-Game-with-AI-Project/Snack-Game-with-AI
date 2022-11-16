import pygame
from pygame import mixer # class that help us handle all kind of music inside our game
from Button_class import *
from button_images import *

# Main class
class MainCLass:
    def __init__(self):
        pygame.init() # Initialize the pygame
        self.screen=pygame.display.set_mode((800,600)) # create the screen
        # music
        self.music=pygame.mixer.music.load('./assets/music.mp3')
        pygame.mixer.music.play(-1)
    
    # Caption and icon
    def caption_and_icon(self):
        pygame.display.set_caption("Snake Game")
        icon= pygame.image.load('./assets/snake.png')
        pygame.display.set_icon(icon)

    # Text
    def text(self):
        font= pygame.font.Font('freesansbold.ttf',32)
        font2= pygame.font.SysFont('timesnewroman',18,bold=False,italic=False)
        text_x=200
        text_y=150
        text= font.render("Welcome to snake game",True,(0,0,0))
        option1_text= font2.render("Play with camera",True,(0,0,0))
        option2_text= font2.render("Play with keyboard",True,(0,0,0))
        self.screen.blit(option1_text,(310,295))
        self.screen.blit(option2_text,(310,395))
        self.screen.blit(text,(text_x,text_y))

    # snake image in the background
    def insert_image(self):
        snake_img= pygame.image.load('./assets/snake_bkg.png')
        snake_x= 370
        snake_y= 50
        self.screen.blit(snake_img,(snake_x,snake_y))
        
    def check_btn(self):
        if option1_btn.draw():
            print('Option 1')
        if option2_btn.draw():
            print('Option 2')
        if mute_btn.draw():
            pygame.mixer.music.stop()
        if low_volume_btn.draw():
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
        if high_volume_btn.draw():
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(1)
    
    
main=MainCLass()

# Game loop
running= True
while running:
    # RGB colors
    main.screen.fill((51,255,255))
    
    if exit_btn.draw():
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    main.check_btn()
    main.insert_image()
    main.text()
    pygame.display.update() # update the game window at each iteration of the code
pygame.quit()