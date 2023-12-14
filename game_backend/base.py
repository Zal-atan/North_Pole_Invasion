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
        self.enemy_direction = 1

        # Sounds
        self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
        self.explosion_sound.set_volume(0.7)
        self.snowball_sound = pygame.mixer.Sound('../audio/woosh.mp3')
        self.snowball_sound.set_volume(0.5)
        self.hit_sound = pygame.mixer.Sound('../audio/snowball_hit.wav')
        self.hit_sound.set_volume(0.6)

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('../fonts/space_invaders.ttf', SCORE_FONT)
        self.font_x = SCREEN_WIDTH / 2 - 70
        self.font_y = 15

        # Health
        self.lives = 3
        self.lives_font = pygame.font.Font('../fonts/space_invaders.ttf', LIVES_FONT)
        self.lives_icon = pygame.image.load('../photos/santa.png').convert_alpha()
        self.lives_icon = pygame.transform.scale(self.lives_icon, LIVES_SIZE)
        self.lives_x = SCREEN_WIDTH - 80
        self.lives_y = 20

        # Game Over
        self.gameover_font = pygame.font.Font('../fonts/space_invaders.ttf', GAME_OVER_FONT)

        # Win Game
        self.win_font = pygame.font.Font('../fonts/space_invaders.ttf', WIN_FONT)


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

    def game_over(self):
        gameover_font = gameover_font.render('SANTA PAYS UP!', True, (0, 0, 0))
        self.screen.blit(gameover_font, (200, 200))

    def collision(self):
        self.hit_sound.play()
        self.explosion_sound.play()

    def score(self):
        score = self.font.render('Score : ' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (self.font_x, self.font_y))

    def lives(self):
        for life in range(self.lives):
            x = self.lives_x + (life * 25)
            self.screen.blit(self.lives_icon, x, self.lives_y)

    def win_game(self):
        win_font = win_font.render('SANTA WINS!', True, (0, 0, 0))
        self.screen.blit(win_font, (200, 200))

    def run_game(self):
        #Updates
        self.player.update()
        self.enemies.update(1)
        self.enemy_snowballs.update()

        # ReDraws
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)
        self.enemies.draw(self.screen)
        self.enemy_snowballs.draw(self.screen)
        self.score()
