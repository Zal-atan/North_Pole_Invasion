""" This files runs the game"""
import pygame
from variables import *
from base import Game


if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize Game
    game = Game(screen)
    clock = pygame.time.Clock()

    # Keep game running while playing
    game_is_on = True
    while game_is_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False
        
        screen.fill((30,30,30))
        game.run_game()

        pygame.display.flip()
        clock.tick(60)
