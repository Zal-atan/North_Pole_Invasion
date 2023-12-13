import pygame
from variables import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../photos/santa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect(midbottom = PLAYER_POSITION)
        self.max_width = SCREEN_WIDTH
        self.speed = PLAYER_SPEED

    def update_player(self):
        print("Hello")
