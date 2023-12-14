import pygame
from variables import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy, x, y):
        super().__init__()

        if enemy == "penguin":
            self.image = pygame.image.load('../photos/penguin.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
            self.rect = self.image.get_rect(topleft = (x, y))
            self.value = 100

        if enemy == "reindeer":
            self.image = pygame.image.load('../photos/reindeer.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
            self.rect = self.image.get_rect(topleft = (x, y))
            self.value = 200

        if enemy == "elf":
            self.image = pygame.image.load('../photos/elf.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
            self.rect = self.image.get_rect(topleft = (x, y))
            self.value = 300

    def update(self, direction):
        self.rect.x += direction

class PapaElf(pygame.sprite.Sprite):
    def __init__(self, start):
        super().__init__()
        self.image = pygame.image.load('../photos/elf.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

