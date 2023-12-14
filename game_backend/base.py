""" This file combines the basic classes together into one game class"""
from player import Player
from background import Background
from enemies import Enemy
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

        # Enemy Creation
        self.enemies = pygame.sprite.Group()
        self.enemy_snowballs = pygame.sprite.Group()
        self.enemy_create()
        self.enemy_direction = 1

        # Sounds
        self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
        self.explosion_sound.set_volume(0.7)

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('../fonts/space_invaders.ttf', 30)
        self.font_x = SCREEN_WIDTH / 2 - 70
        self.font_y = 15

    # Enemy Create
    def enemy_create(self):
        for row in range(1, ENEMY_ROWS + 1):
            for column in range(1, ENEMY_COLUMNS + 1):
                x = column * ENEMY_X_SPACING + ENEMY_X_START_SPACING
                y = row * ENEMY_Y_SPACING + ENEMY_Y_START_SPACING
            
                if row <= 2: 
                    enemy_img = Enemy("elf", x, y)
                elif row == 3:
                    if column == 4:
                        enemy_img = Enemy("rudolph", x, y)
                    else:
                        enemy_img = Enemy("reindeer", x, y)
                else:
                    enemy_img = Enemy("penguin", x, y)
                self.enemies.add(enemy_img)

        # Game Over


    def collision(self):
        self.explosion_sound.play()

    def score(self):
        score = self.font.render('Score : ' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (self.font_x, self.font_y))

    def run_game(self):
        #Updates
        self.player.update()

        # ReDraws
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)
        self.enemies.draw(self.screen)
        self.score()
