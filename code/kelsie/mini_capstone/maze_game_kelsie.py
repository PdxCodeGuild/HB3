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
tile_size = 32

tree = (0, 255, 0)
path = (160, 82, 45)

color = (160, 82, 45)
world_x = tile_size * 20
world_y = tile_size * 15
screen = pygame.display.set_mode((world_x, world_y))

player1_x = 0   # starting coordinates
player1_y = 0
player1 = pygame.draw.rect(screen, (255,0,0), (player1_x, player1_y, tile_size, tile_size))

backdropbox = screen.get_rect()
steps = 5

def create_texture(color):
    image = pygame.Surface((tile_size,tile_size))
    image.fill(color)
    return image

textures = {
    0 : create_texture(tree),
    0 : create_texture(path)
}


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




def draw_map(screen, level):
    MAP_HEIGHT = len(level) 
    MAP_WIDTH = len(level[0])
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            screen.blit(textures[level[row][col]],
                        (col*tile_size, row*tile_size))    



#for row in range(len(level)):
#    for column in range(len(level[row])):
#        wall = pygame.draw.rect(screen, (0, 255, 0), (row, column, 64, 64))
#        screen.blit(screen, backdropbox) 

def main():
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
       
