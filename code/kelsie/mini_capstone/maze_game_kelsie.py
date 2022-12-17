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

pygame.init()


""" variables"""
world_x = 960
world_y = 720
fps = 40
ani = 4
color = (255, 0, 0)
running = True
player1_x = 0
player1_y = 0

# horizontal walls
   # pygame.draw.rect(screen, (0, 255, 0), (48, 0, 936, 24)) # row 1
    # vertical walls
#pygame.draw.rect(screen, (0, 255, 0), (936, 24, 24, 696)) # column 1
#pygame.draw.rect(screen, (0, 255, 0), (96, 120, 24, 96))#vert wall 2
#pygame.draw.rect(screen, (0, 255, 0), (144, 192, 24, 120))  # vert wall 3
#pygame.draw.rect(screen, (0, 255, 0), (120, 48, 24, 24))  # vert wall 4
#pygame.draw.rect(screen, (0, 255, 0),  (168, 96, 24, 24)) # vert wall 5
#pygame.draw.rect(screen, (0, 255, 0), (240, 120, 24, 168))  # vert wall 6
#pygame.draw.rect(screen, (0, 255, 0), (336, 144, 24, 120))  # vert wall 7
#pygame.draw.rect(screen, (0, 255, 0), (360, 192, 24, 48))  # vert wall 8
#pygame.draw.rect(screen, (0, 255, 0), (408, 240 ,24, 48))  # vert wall 9
#pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 10
#pygame.draw.rect(screen, (0, 255, 0), (,,24,))  # vert wall 11
#pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 12
#pygame.draw.rect(screen, (0, 255, 0),(,,24,))   # vert wall 13
#pygame.draw.rect(screen, (0, 255, 0), (0, 24, 24, 696)) # vert wall 14



clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([world_x, world_y])
world.fill(color)
backdropbox = world.get_rect()
world.blit(world, backdropbox)
steps = 5

def main():
        while running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:   # setting game exit options
                                running = False

                key_pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            #if event.key == ord('q'):
                #running = False
                if key_pressed[pygame.K_ESCAPE] :
                        running = False
                if key_pressed[pygame.K_LEFT] :
                        player1_x -= steps
                if key_pressed[pygame.K_RIGHT]:
                        player1_x += steps
                if key_pressed[pygame.K_UP] :
                        player1_y -= steps
                if key_pressed[pygame.K_DOWN] :
                        player1_y += steps
                world.fill(color)
                pygame.display.flip()
                clock.tick(fps)
       
