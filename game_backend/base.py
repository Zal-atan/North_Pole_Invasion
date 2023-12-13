""" This file combines the basic classes together into one game class"""
from player import Player
import pygame
from variables import *

class Game:
    def __init__(self, screen):
        
        #Screen
        self.screen = screen
        # Player Creation
        player_img = Player()
        self.player = pygame.sprite.GroupSingle(player_img)

    def run_game(self):
        # self.player.update_player()
        self.player.draw(self.screen)
