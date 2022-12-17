import pygame
import random

from pygame.locals import (    # these are the arrow key commands, the escape key, 
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()


""" variables"""
tile_size = 32

tree = (0, 255, 0)
path = (160, 82, 45)

color = (160, 82, 45)
world_x = tile_size * 10
world_y = tile_size * 10
screen = pygame.display.set_mode((world_x, world_y))

player1_x = 0   # starting coordinates
player1_y = 0
player1 = pygame.draw.rect(screen, (255,0,0), (player1_x, player1_y, tile_size, tile_size))

backdropbox = screen.get_rect()
steps = 5

#def create_texture(color):
#    image = pygame.Surface((tile_size,tile_size))
#    image.fill(color)
#    return image

#textures = {
#    1 : create_texture(tree),
#    0 : create_texture(path)
#}

# horizontal walls
   # pygame.draw.rect(screen, (0, 255, 0), (48, 0, 936, 24)) # row 1
    # vertical walls
pygame.draw.rect(screen, (0, 255, 0), (936, 24, 24, 696)) # column 1
pygame.draw.rect(screen, (0, 255, 0), (96, 120, 24, 96))#vert wall 2
pygame.draw.rect(screen, (0, 255, 0), (144, 192, 24, 120))  # vert wall 3
pygame.draw.rect(screen, (0, 255, 0), (120, 48, 24, 24))  # vert wall 4
pygame.draw.rect(screen, (0, 255, 0),  (168, 96, 24, 24)) # vert wall 5
pygame.draw.rect(screen, (0, 255, 0), (240, 120, 24, 168))  # vert wall 6
pygame.draw.rect(screen, (0, 255, 0), (336, 144, 24, 120))  # vert wall 7
pygame.draw.rect(screen, (0, 255, 0), (360, 192, 24, 48))  # vert wall 8
pygame.draw.rect(screen, (0, 255, 0), (408, 240 ,24, 48))  # vert wall 9
#pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 10
#pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 11
#pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 12
#pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 13
#pygame.draw.rect(screen, (0, 255, 0), (0, 24, 24, 696)) # vert wall 14



#def draw_map(screen, level):
#    MAP_HEIGHT = len(level) 
#    MAP_WIDTH = len(level[0])
#    for row in range(MAP_HEIGHT):
#        for col in range(MAP_WIDTH):
#            screen.blit(textures[level[row][col]],
#                        (col*tile_size, row*tile_size))    



#for row in range(len(level)):
#    for column in range(len(level[row])):
#        wall = pygame.draw.rect(screen, (0, 255, 0), (row, column, 64, 64))
#        screen.blit(screen, backdropbox) 

def main():
    player1_x = 0   # starting coordinates
    player1_y = 0
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

player1 = pygame.draw.rect(screen, (255,0,0), (player1_x, player1_y, tile_size, tile_size))
screen.blit(screen, backdropbox)
pygame.display.flip()
       
