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
                
                for wall in walls :                             # stopping the player when there is a collision with the wall
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
screen = pygame.display.set_mode((tile_size * 32, tile_size * 15))


walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                              W",
"W    W    WWWWWWWWWWWW    WWWWWW",
"W   WWWW       W               W",
"W   W        WWWWWWWWWWWWWW  WWW",
"W WWW  WWWW      W             W",
"W   W     W W        W   WWWW  W",
"W   W     W   WWW  WWWWWWWW    W",
"W   WWW WWW   W W        W   WWW",
"W     W   W   W W   W  WWW     W",
"WWW   W   WWWWW WWWWW    WWWWWWW",
"W WW      W         W          W",
"W W   WWWW   WWW  WWW  WWWWW   W",
"W     WE     W         W       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


x = y = 0
for row in level:
        for col in row:
                if col == "W":
                        Wall((x, y))
                if col == "E":
                        end_rect = pygame.Rect(x, y, 16, 16)
                x += 16
        y += 16
        x = 0

running = True
while running:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN and event.key == ord('q') :
                running = False

        key = pygame.key.get_pressed() # this tells the player to move 2 pixels when the arrow keys or wasd are pressed
        if key[pygame.K_LEFT] or key[pygame.K_a] :
                player.move(-2, 0)
        if key[pygame.K_RIGHT] or key[pygame.K_d] :
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
                pygame.draw.rect(screen, (0, 110, 51), wall.rect)
                pygame.draw.rect(screen, (255, 0, 0), end_rect)
                pygame.draw.rect(screen, (255, 200, 0), player.rect)

        pygame.display.flip()
        

pygame.quit()