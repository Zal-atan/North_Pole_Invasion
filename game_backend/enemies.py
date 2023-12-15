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

        if enemy == "rudolph":
            self.image = pygame.image.load('../photos/rudolph.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
            self.rect = self.image.get_rect(topleft = (x, y))
            self.value = 300

        if enemy == "elf":
            self.image = pygame.image.load('../photos/elf.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, ELF_SIZE)
            self.rect = self.image.get_rect(topleft = (x, y))
            self.value = 300

    def update(self, direction, move_down=0):
        self.rect.x += direction
        self.rect.y += ENEMY_MOVEDOWN * move_down

class Tinseltoe(pygame.sprite.Sprite):
    def __init__(self, start_side):
        super().__init__()
        self.image = pygame.image.load('../photos/tinsletoe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, ENEMY_SIZE)

        if start_side == 'right':
            x = SCREEN_WIDTH + 50
            self.speed = -3

        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x, 80))

    def update(self):
        self.rect.x += self.speed
