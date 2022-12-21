import pygame
import sys




from pygame.locals import (    # these are the arrow key commands, the escape key, 
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_a,
    K_w,
    K_d,
    K_s,
    K_q,
    KEYDOWN,
    QUIT,
)

pygame.init()



class Player (object) :                 # creating a class for the player and the player movements
        def __init__(self) :
                self.rect = pygame.Rect(32, 32, 16, 16) # this creates the player rectangle

        def move(self, dx, dy) :
                if dx != 0 :
                        self.move_single_axis(dx, 0)    # move() tells the player exactly how to move
                if dy != 0 :
                        self.move_single_axis(0, dy)

        def move_single_axis(self, dx, dy) :    # move_single_axis does the math for the specified movement
                self.rect.x += dx
                self.rect.y += dy
                
                for wall in walls :                             # but stopping the player when there is a collision with the wall
                        if self.rect.colliderect(wall.rect) :   
                                if dx > 0 :
                                        self.rect.right = wall.rect.left
                                if dx < 0 :
                                        self.rect.left = wall.rect.right
                                if dy > 0 :
                                        self.rect.bottom = wall.rect.top
                                if dy < 0 :
                                        self.rect.top = wall.rect.bottom



class Wall(object) :
        def __init__(self, pos) :
                walls.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 16, 16)




       
pygame.display.set_caption("Lost in the Woods")
tile_size = 16
screen = pygame.display.set_mode((tile_size * 50, tile_size * 28)) # set the screen size


walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W               W                             W  W",
"W    W    WWWWWWWWWWWW    WWWWW  WWWW  WWWWWWWW  W",
"W   WWWW       W                    W            W",
"W   W        WWWWWWWWWWWWWW  WW     WWWWW   WWW  W",
"W WWW  WWWW      W                            W  W",
"W   W     W W        W   WWWW  WWWWWWWWWW   WWWWWW",
"W   W   W W   WWW  WWWWWWWW    W        W        W",
"W   WWW WWW   W W        W   WWW  WWWW  WW  W    W",
"W     W   W   W W   W  WWW           W      W  WWW",
"WWW   W   WWWWW WWWWW    WWWWWWWWWWWWWWWWW  W    W",
"W WW      W         W             W         WWW  W",
"W W   WWWW   WWW  WWWWWWWWWW  WWWWWWWWW   WWW    W",
"W     W      W         W          W              W",
"WWWWWWWWWW  WWWWWWW  WWWWWWWWWW   WW  WWWWWWWWW  W",
"W            W         W          W      W       W",
"WWWW  WWWWWWWW     W     WWWWWWW  W  W   W       W",
"W         W  W   WWWWWWWWW        W  W   W  WWWWWW",
"W  W  W      W           W   W       W           W",
"W  WWWW WWW   WWW        W   WWW  WWWW  WW  W    W",
"W     W   W   W EW  W  WWW           W  W   W  WWW",
"WWW   W   WWWWW  WWWW    WWWWWWWWWWWWWWWWW  W    W",
"W WW      W         W           W   W       WWW  W",
"W W   WWWW   WWWWWWWW  WWWWW    W   W  WWWWWW    W",
"W     W      W   W     W      W     W         W  W",
"WWW  WWWWW   W   W   WWWW    WW   WWWW  W  WWWWWWW",
"W                    W                  W        W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


x = 0 
y = 0
for row in level:
        for col in row:
                if col == "W":
                        Wall((x, y)) # calling on the Wall class to create a wall at the specified coordinates
                if col == "E":
                        end_rect = pygame.Rect(x, y, 16, 16) # creating the end rectangle at "E"
                x += 16
        y += 16         # tile size is 16px so each change in coordinate being checked is 16px 
        x = 0

running = True
while running:
        key = pygame.key.get_pressed() # variable for storing pressed keys
        for event in pygame.event.get():
                if event.type == pygame.QUIT:   # can quit game with the x button, esc key, or q
                        running = False
                if  key[pygame.K_ESCAPE]:
                        running = False
                if  key[pygame.K_q] :
                        running = False

        if key[pygame.K_LEFT] or key[pygame.K_a] :      # this tells the player to move 2 pixels when the arrow keys or wasd are pressed
                player.move(-2, 0)                      # the placement here lets the character glide smoothly when holding down a key
        if key[pygame.K_RIGHT] or key[pygame.K_d] :     # rather then having to press the key for every two pixels of movement
                player.move(2, 0)
        if key[pygame.K_UP] or key[pygame.K_w] :
                player.move(0, -2)
        if key[pygame.K_DOWN] or key[pygame.K_s] :
                player.move(0, 2)


        if player.rect.colliderect(end_rect):   # when the player reaches the end, the game exits
                pygame.quit()
                sys.exit()


        screen.fill((196, 164, 132))
        for wall in walls:
                pygame.draw.ellipse(screen, (0, 110, 51), wall.rect) # draws the walls as circles to represent trees
                pygame.draw.rect(screen, (92, 64, 51), end_rect) # end rectangle is dark brown like a door
                pygame.draw.ellipse(screen, (255, 200, 0), player.rect) # draws player.rect as a circle

        pygame.display.flip()
        

pygame.quit()
