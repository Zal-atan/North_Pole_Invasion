import pygame
from variables import *
from projectiles import Present

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../photos/santa.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect(midbottom = PLAYER_POSITION)
        self.max_width = SCREEN_WIDTH - PLAYER_SIZE[0]
        self.speed = PLAYER_SPEED
        self.ready_to_throw = True
        self.present_cooldown_ticks = PLAYER_THROW_COOLDOWN
        self.present_cooldown = 0

        self.presents = pygame.sprite.Group()

    def user_input(self):
        """Checks for key presses, right arrow or "d" to move right,
        left arrow or "a" to move left"""
        keys = pygame.key.get_pressed()

        # Right key or "D"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.x >= self.max_width:
                pass
            else:
                self.rect.x += self.speed
        # Left Key or "A"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.x <= 0:
                pass
            else:
                self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready_to_throw:
            self.throw_present()

    def throw_present(self):
        self.presents.add(Present(self.rect.center))
        self.ready_to_throw = False
        self.present_cooldown = pygame.time.get_ticks()
        # Play sound?

    def get_present_cooldown(self):
        if not self.ready_to_throw:
            time_now = pygame.time.get_ticks()
            # print(f"timeNow: {time_now}, present_cooldown : {self.present_cooldown} =  ")
            if time_now - self.present_cooldown >= self.present_cooldown_ticks:
                self.ready_to_throw = True

    def update(self):
        self.user_input()
        self.get_present_cooldown()
        self.presents.update()
