""" This file combines the basic classes together into one game class"""
from player import Player
from background import Background
from enemies import Enemy
from projectiles import Snowball
import pygame
from variables import *
from pygame import mixer
from random import choice

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
        self.enemy_direction = -1
        self.enemy_move_down = 0

        # Sounds
        self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
        self.explosion_sound.set_volume(0.7)
        self.snowball_sound = pygame.mixer.Sound('../audio/snowball.wav')
        self.snowball_sound.set_volume(0.5)

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('../fonts/space_invaders.ttf', 30)
        self.font_x = SCREEN_WIDTH / 2 - 70
        self.font_y = 15

        # Game Over
        self.gameover_font = pygame.font.Font('../fonts/space_invaders.ttf', GAME_OVER_FONT)


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

    # Throw Snowball
    def throw_snowball(self):
        if self.enemies.sprites():
            random_enemy = choice(self.enemies.sprites())
            snowball_img = Snowball(random_enemy.rect.center)
            self.enemy_snowballs.add(snowball_img)
            self.snowball_sound.play()

    # Check Enemies hitting wall
    def check_hit_wall(self):
        all_enemies = self.enemies.sprites()
        for enemy in all_enemies:
            if (enemy.rect.right >= SCREEN_WIDTH) or (enemy.rect.left <= 0):
                self.enemy_direction *= -1
                self.enemies.update(self.enemy_direction * 2, 1)


    def game_over(self):
        gameover_font = gameover_font.render('GAME OVER', True, (0, 0, 0))
        self.screen.blit(gameover_font, (200, 200))

    def collision(self):
        self.explosion_sound.play()

    def score(self):
        score = self.font.render('Score : ' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (self.font_x, self.font_y))

    def run_game(self):
        #Updates
        self.player.update()
        self.enemies.update(self.enemy_direction)
        self.check_hit_wall()
        self.enemy_snowballs.update()

        # ReDraws
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)
        self.enemies.draw(self.screen)
        self.enemy_snowballs.draw(self.screen)
        self.score()
