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
    def __init__(self, screen, sound):

        #Screen
        self.screen = screen
        self.sound = sound

        # Background
        bg = Background()
        self.bg = pygame.sprite.GroupSingle(bg)

        # Player Creation
        player_img = Player(self.sound)
        self.player = pygame.sprite.GroupSingle(player_img)

        # Enemy Creation
        self.enemies = pygame.sprite.Group()
        self.enemy_snowballs = pygame.sprite.Group()
        self.enemy_create()
        self.enemy_direction = -1
        self.enemy_move_down = 0

        # Sounds
        if self.sound:
            self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
            self.explosion_sound.set_volume(0.7)
            self.snowball_sound = pygame.mixer.Sound('../audio/whoosh.mp3')
            self.snowball_sound.set_volume(0.5)
            self.hit_sound = pygame.mixer.Sound('../audio/snowball_hit.wav')
            self.hit_sound.set_volume(0.6)

        # Score
        self.score_value = 0
        self.font = pygame.font.Font('../fonts/space_invaders.ttf', SCORE_FONT)
        self.font_x = SCREEN_WIDTH / 2 - 70
        self.font_y = 15
        self.game_is_over = 0

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
            if self.sound:
                self.snowball_sound.play()

    # Check Enemies hitting wall
    def check_hit_wall(self):
        all_enemies = self.enemies.sprites()
        for enemy in all_enemies:
            if (enemy.rect.right >= SCREEN_WIDTH) or (enemy.rect.left <= 0):
                self.enemy_direction *= -1
                self.enemies.update(self.enemy_direction * 2, 1)

    # Check for impacts
    def check_impacts(self):

        # presents
        if self.player.sprite.presents:
            for present in self.player.sprite.presents:

                enemy_hit = pygame.sprite.spritecollide(present,
                                                        self.enemies,
                                                        True,
                                                        pygame.sprite.collide_rect_ratio(0.5))
                if enemy_hit:
                    for enemy in enemy_hit:
                        self.score_value += enemy.value
                    present.kill()
                    if self.sound:
                        self.explosion_sound.play()
                        # explosion sound?

        # snowballs
        if self.enemy_snowballs:
            for snowball in self.enemy_snowballs:
                if pygame.sprite.spritecollide(snowball,
                                                self.player,
                                                False,
                                                pygame.sprite.collide_rect_ratio(0.5)):
                    snowball.kill()
                    if self.sound:
                        self.hit_sound.play()
                        #santa hit sound
                    self.lives -= 1
                    if self.lives <= 0:
                        print("YOU LOSE SUCKER")
                        self.game_is_over = 1
                        # pygame.quit()


    def game_over(self):
        gameover_font = self.gameover_font.render('SANTA PAYS UP!', False, (0, 0, 0))
        self.screen.blit(gameover_font, (100, 200))

    def score(self):
        score = self.font.render('Score : ' + str(self.score_value), True, (0, 0, 0))
        self.screen.blit(score, (self.font_x, self.font_y))

    def display_lives(self):
        x_offset = 10
        lives_text = self.lives_font.render('Lives: ', False, (0, 0, 0))
        self.screen.blit(lives_text, (x_offset, self.lives_y))
        # Adds space after lives text
        x_offset += lives_text.get_width() + 10

        # Adds space between icons
        for _ in range(self.lives):
            self.screen.blit(self.lives_icon, (x_offset, self.lives_y))
            x_offset += self.lives_icon.get_width() + 5

    def win_game(self):
        win_font = self.win_font.render('SANTA WINS!', True, (0, 0, 0))
        self.screen.blit(win_font, (200, 200))

    def run_game(self):
        #Updates
        if not self.game_is_over:
            self.player.update()
            self.enemies.update(self.enemy_direction)
            self.check_hit_wall()
            self.enemy_snowballs.update()
            self.check_impacts()

            if len(self.enemies) == 0:
                self.game_is_over = 2
        # ReDraws
        self.bg.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.presents.draw(self.screen)
        self.enemies.draw(self.screen)
        self.enemy_snowballs.draw(self.screen)
        self.score()
        self.display_lives()
        if self.game_is_over:
            self.bg.draw(self.screen)
            self.score()
            self.game_over()
        if self.game_is_over == 2:
            self.bg.draw(self.screen)
            self.score()
            self.win_game()
