import pygame
from variables import *

class Present(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('../photos/present.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PRESENT_SIZE)
        self.rect = self.image.get_rect(center = position)
        self.speed = PRESENT_SPEED

    def destroy(self):
        """ Destroys present if it goes above screen """
        if self.rect.y >= SCREEN_HEIGHT + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()

class Snowball(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('../photos/present.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PRESENT_SIZE)
        self.rect = self.image.get_rect(center = position)
        self.speed = PRESENT_SPEED

    def destroy(self):
        """ Destroys present if it goes above screen """
        if self.rect.y >= SCREEN_HEIGHT + 50:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.destroy()
