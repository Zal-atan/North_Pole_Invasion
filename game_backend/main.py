import pygame
import sys
from variables import *
from player import Player
# from base import Game


class Game:
    def __init__(self):
        
        #Screen
        # Player Creation
        player_img = Player()
        self.player = pygame.sprite.GroupSingle(player_img)

    def run_game(self):
        self.player.draw(screen)
        # self.player.update_player()

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize Game
    game = Game()
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
