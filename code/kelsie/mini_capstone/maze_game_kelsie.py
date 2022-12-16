import pygame

#from pygame.locals import (    # these are the arrow key commands, the escape key, 
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
#    QUIT,
#)

pygame.init()


""" variables"""

running = True
color = (234, 221, 202)
#rectangle_color = (255, 0, 0)
#steps = 10 # how many pixels the player moves

"""Objects"""



"""setup"""

#window.fill(color)
#pygame.display.flip()
#pygame.display.set_caption("Lost In The Woods")



#player1 = pygame.draw.rect(window, (255,0,0), (player1_x, player1_y, player1_width, player1_height)) # Create the player
steps = 5 # how many pixels the player moves
tiles = ['empty.png', 'wall.png', 'goal.png']
tile_size = 64
world_x = tile_size * 20
world_y = tile_size * 15
screen = pygame.display.set_mode((world_x, world_y)) # set the screen size and color
backdropbox = screen.get_rect()

level = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

for row in range(len(level)):
    for column in range(len(level[row])):
        pygame.draw.rect(screen, (0, 255, 0), (row, column, 64, 64))
        

player1_x = 0   # starting coordinates
player1_y = 0
player1 = pygame.draw.rect(screen, (255,0,0), (player1_x, player1_y, tile_size, tile_size))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # setting game exit options
                running = False

    key_pressed = pygame.key.get_pressed()
        #if event.type == pygame.KEYDOWN:
            #if event.key == ord('q'):
                #running = False
    if key_pressed[pygame.K_ESCAPE] :
                running = False
    if key_pressed[pygame.K_LEFT] :
                player1_x -= steps
                #player1.move(-steps,0)
    if key_pressed[pygame.K_RIGHT]:
                #player1.move(steps,0)
                player1_x += steps
    if key_pressed[pygame.K_UP] :
                #player1.move(0, steps)
                player1_y -= steps
    if key_pressed[pygame.K_DOWN] :
                #player1.move(-steps, 0)
                player1_y += steps

screen.fill(color)
    # horizontal walls
   # pygame.draw.rect(screen, (0, 255, 0), (48, 0, 936, 24)) # row 1
    # vertical walls
   # pygame.draw.rect(screen, (0, 255, 0), (936, 24, 24, 696)) # vert wall 1
   # pygame.draw.rect(screen, (0, 255, 0), (96, 120, 24, 96))#vert wall 2
   # pygame.draw.rect(screen, (0, 255, 0), (144, 192, 24, 120))  # vert wall 3
   # pygame.draw.rect(screen, (0, 255, 0), (120, 48, 24, 24))  # vert wall 4
   # pygame.draw.rect(screen, (0, 255, 0),  (168, 96, 24, 24)) # vert wall 5
   # pygame.draw.rect(screen, (0, 255, 0), (240, 120, 24, 168))  # vert wall 6
   # pygame.draw.rect(screen, (0, 255, 0), (336, 144, 24, 120))  # vert wall 7
   # pygame.draw.rect(screen, (0, 255, 0), (360, 192, 24, 48))  # vert wall 8
   # pygame.draw.rect(screen, (0, 255, 0), (408, 240 ,24, 48))  # vert wall 9
   # pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 10
   # pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 11
   # pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 12
   # pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 13
    #pygame.draw.rect(screen, (0, 255, 0), (0, 24, 24, 696)) # vert wall 14
    
    
  
pygame.draw.rect(screen, (255,0,0), (player1_x, player1_y, 64, 64))
screen.blit(screen, backdropbox)
pygame.display.flip()
       
