""" This file combines the basic classes together into one game class"""
from player import Player
from background import Background
import pygame
from variables import *

class Game:
    def __init__(self, screen):
        
        #Screen
        self.screen = screen

        # Background
        bg = Background()
        self.bg = pygame.sprite.GroupSingle(bg)

        # Player Creation
        player_img = Player()
        self.player = pygame.sprite.GroupSingle(player_img)

    def run_game(self):
        self.player.update()
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)
