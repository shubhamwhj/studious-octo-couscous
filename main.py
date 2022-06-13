import pygame, sys, random
from game import create_screen, screen_height, gameplay


screen = create_screen()

player_surf = pygame.image.load("assets/joe.png").convert_alpha()
player_surf = pygame.transform.scale(player_surf, (40, 63))

player_rect = pygame.Rect(550, screen_height - 145 ,40,63) # x, y, width, height

while True:
    gameplay()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(player_surf,player_rect)

    pygame.display.update()
