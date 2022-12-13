import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player() :                            # creating the player square and how it functions
    def __init__(self) :                    # the player square is slightly smaller than each stepping square
        self.rect = pygame.Rect(32, 32, 16, 16)
        screen.blit(self.rect(screen, rect_color, ))
        pygame.display.flip()

    def move(self, dx, dy) :                # this shows how the players square moves
        if dx != 0 :
            self.move_one_space(dx, 0)
        if dy != 0 :
            self.move_one_space(0, dy)

    def move_one_space(self, dx, dy) :      # this defines the movements
        self.rect.x += dx
        self.rect.y += dy




pygame.init()


screen = pygame.display.set_mode((800, 600)) # set the screen size
color = (85, 107, 47)
screen.fill(color)
pygame.display.flip()

walls = [] # List to hold the walls
player1 = Player() # Create the player

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


running = True
while running == True :                     
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False                # ending the game when the user chooses quit


rect_color = (255, 0, 0)
player_rect = pygame.draw.rect(screen, rect_color, pygame.Rect(30, 30, 60, 60))
screen.blit(player_rect(0, 0))
pygame.display.flip()