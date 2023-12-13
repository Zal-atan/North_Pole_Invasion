import pygame
import sys


if __name__ == "__main__":
    # Initialize pygame
    pygame.init

    # Initialize screen
    screen_height = 800
    screen_width = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # pygame.display.flip()
    game_is_on = True
    while game_is_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False
