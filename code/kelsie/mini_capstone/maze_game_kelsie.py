import pygame

from pygame.locals import (    # these are the arrow key commands, the escape key, 
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


""" variables"""
world_x = 960
world_y = 720
fps = 40            # frames per second
ani = 4             # animation cycles
running = True
color = (85, 107, 47)

"""Objects"""

class Player() :                            # creating the player square and how it functions
    def __init__(self) :                    
        self.rect = pygame.Rect(0, 0, 24, 24)
        






"""setup"""
screen = pygame.display.set_mode((world_x, world_y)) # set the screen size and color
screen.fill(color)
pygame.display.flip()

clock = pygame.time.Clock # set a timer
pygame.init()
player1 = Player() # Create the player
player1.rect.x = 0
player1.rect.y = 0
#player_list = pygame.sprite.Group()
#player_list.add(player1)

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                      W",
    "W     W    WWWWWWWWWWWWWWWWWWWWWWW     W",
    "W   WWWWW          W             W     W",
    "W       W    WWWWWWWWWWWW  WWWWWWW     W",
    "W WWW  WWWW             W           W  W",
    "W   W     W   W   WW  WWW  WWWWWWW  W  W",
    "W   W     W   WWW W     W     W     W  W",
    "W   WWW WWW   W W    W   WWWWWWWWWWWW  W",
    "W     W   W   W    W W                 W",
    "WWW   W   WWWWW WWWWWWWWWWW  WWWW   WWWW",
    "W     W  WW      W               W     W",
    "W     WWWW   WWWWWWW   WWWWWWW  WWWWWWWW",
    "W E            W           W           W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


"""Main loop"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # setting game exit options
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                running = False
        screen.blit(screen, )
        #player_list.draw(screen)
        pygame.display.flip()
        #clock.tick(fps)#
