""" This files runs the game"""
import pygame
from variables import *
from base import Game
from pygame import mixer



if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize Game
    game = Game(screen)
    clock = pygame.time.Clock()

    #audio
    music = pygame.mixer.Sound('../audio/background_music.wav')
    music.set_volume(0.2)
    music.play(-1)

    SNOWBALL = pygame.USEREVENT + 1
    pygame.time.set_timer(SNOWBALL, ENEMY_THROW_COOLDOWN)
    
    # Keep game running while playing
    game_is_on = True
    while game_is_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False
            if event.type == SNOWBALL:
                game.throw_snowball()
        
        screen.fill((30,30,30)) # Clears the screen each cycle with blank screen
        game.run_game()

        pygame.display.flip()
        clock.tick(60)

