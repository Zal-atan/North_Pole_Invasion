""" This file combines the basic classes together into one game class"""
from player import Player
from background import Background
import pygame
from variables import *
from pygame import mixer

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

        # Sounds
        self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
        self.explosion_sound.set_volume(0.7)

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('../fonts/space_invaders.ttf', 30)
        font_x = SCREEN_WIDTH / 2
        font_y = SCREEN_HEIGHT - 40

        # Game Over

    def run_game(self):
        #Updates
        self.player.update()

        # ReDraws
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)

    def collision(self):
        self.explosion_sound.play()

    def score(self, x, y):
        score = self.font.render('Score : ' + str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (x, y))
