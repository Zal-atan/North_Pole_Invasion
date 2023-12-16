import pygame
from variables import *

class Igloo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.images = {
            1: pygame.image.load('../photos/igloo_obstacles/obstacle1.png').convert_alpha(),
            2: pygame.image.load('../photos/igloo_obstacles/obstacle2.png').convert_alpha(),
            3: pygame.image.load('../photos/igloo_obstacles/obstacle3.png').convert_alpha(),
            4: pygame.image.load('../photos/igloo_obstacles/obstacle4.png').convert_alpha(),
            5: pygame.image.load('../photos/igloo_obstacles/obstacle5.png').convert_alpha(),
            6: pygame.image.load('../photos/igloo_obstacles/obstacle6.png').convert_alpha(),
            7: pygame.image.load('../photos/igloo_obstacles/obstacle7.png').convert_alpha(),
            8: pygame.image.load('../photos/igloo_obstacles/obstacle8.png').convert_alpha(),
            9: pygame.image.load('../photos/igloo_obstacles/obstacle9.png').convert_alpha(),
            10: pygame.image.load('../photos/igloo_obstacles/obstacle10.png').convert_alpha(),
        }

        self.img = 1
        self.image = pygame.transform.scale(self.images[self.img], IGLOO_SIZE)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.hitpoints = 10


    def update(self):
        self.image = pygame.transform.scale(self.images[self.img], IGLOO_SIZE)
