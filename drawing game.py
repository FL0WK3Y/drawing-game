import pygame
import os 
from pygame.locals import *
pygame.init()
# this is my display window 
screen = pygame.display.set_mode((800,600),0,32)

# this is my button's size, color,font and location 
text_color = (255,255,0)
button_color = (0,0,170)
button_over_color = (255, 20, 20)
button_width = 100
button_height = 50
button_rect = [screen.get_width()/2 - button_width/2,screen.get_height()/2 - button_height/2, button_width, button_height , ]
button_font = pygame.font.SysFont('Arial', 10)
button_text = button_font.render('DO NOT CLICK',True,text_color)
screen.fill((100,100,100))
# this is my sprite 
snake1 = pygame.image.load(os.path.join('/Users/gregorirodriguez/Desktop/Udemy_Games/drawing_game/images/sel.png'))
spriteWidth = 32
spriteheight = 32

snake1 = pygame.transform.scale(snake1,(spriteWidth,spriteheight))
#this is the the title of the game window  
pygame.display.set_caption("DO NOT CLICK THE RECTANGLE")
screen.fill((225,225,225))


game_over = False

# this is the possition of the sprite
x, y =(0,0)
clock= pygame.time.Clock()
# this while loop will run the window until the variable for game_over changes to True
while not game_over:
    # this is the change in timeduring the frame
    dt = clock.tick(100)

    for event in pygame.event.get():
        # this is to check if the window is still open  if the window is closed then it quits the program 
        if event.type == pygame.QUIT:
            # if this is true the game has eneded
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]  ):
                game_over = True
        if event.type ==pygame.MOUSEMOTION:
            x,y =event.pos
    if(button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
        pygame.draw.rect(screen,button_over_color, button_rect)   
        pygame.display.update()

    pressed = pygame.key.get_pressed()
    # this is to move the sprite up 
    if pressed[K_UP]:
        y-=.5 * dt #  dt multiply that amount of movement by your change in time during the frame.
    
    # this is to move the sprite down
    if pressed[K_DOWN]:
        y+=.5 * dt #
    
    #this is to move the sprite left
    if pressed[K_LEFT]:
        x-=.5 * dt
    
    #this to meve the sprite right
    if pressed [K_RIGHT]:
        x +=.5* dt
    if pressed [K_SPACE]:
        x=0 
        y=0
    # the code below this is creating a border so that the sprite can't leave the restricted era 
    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth
    if y > (screen.get_height() - spriteheight):
        y = screen.get_height() - spriteheight
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    elif event.type ==pygame.MOUSEMOTION:
        x,y = event.pos
        x -= spriteWidth/2
        y -= spriteheight/2 
    

    #screen.fill((255,255,255))
    # this is to display the sprite on the screen 
    screen.blit(snake1, (x,y))
 
# this is creating the button on the game window 

    pygame.draw.rect(screen,button_color, button_rect)
    # this makes the rectangle button visible and put the name of the button in the center of the rectangle 
    screen.blit(button_text, (button_rect[0]+ (button_width - button_text.get_width())/2, button_rect[1] + (button_height - button_text.get_height())/2))
   # this is my update method to update my game display
    pygame.display.update()

pygame.quit()
