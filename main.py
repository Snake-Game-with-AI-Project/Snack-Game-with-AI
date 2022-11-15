import pygame

# Main class
class MainCLass:
    def __init__(self):
        pygame.init() # Initialize the pygame
        self.screen=pygame.display.set_mode((800,600)) # create the screen

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
    
# Button class
class Button(MainCLass):
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
    
main=MainCLass()

#load btn imgs
option1_img= pygame.image.load('./assets/option1.png').convert_alpha()
option2_img= pygame.image.load('./assets/option2.png').convert_alpha()
exit_img= pygame.image.load('./assets/exit.png').convert_alpha()

# create buttons
option1_btn=Button(300,230,option1_img,0.7)
option2_btn=Button(300,330,option2_img,0.7)
exit_btn= Button(300,430,exit_img,0.7)

# Game loop
running= True
while running:
    # RGB colors
    main.screen.fill((51,255,255))
    if option1_btn.draw():
        print('Option 1')
    if option2_btn.draw():
        print('Option 2')
    if exit_btn.draw():
        running=False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    main.insert_image()
    main.text()
    pygame.display.update() # update the game window at each iteration of the code
pygame.quit()