""" This file combines the basic classes together into one game class"""
from player import Player
from background import Background
from enemies import Enemy, Tinseltoe
from projectiles import Snowball
import pygame
from variables import *
from pygame import mixer
from random import choice, randint

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
        # self.enemy_create()
        self.enemy_direction = -1
        self.enemy_move_down = 0

        self.tinseltoe = pygame.sprite.GroupSingle()
        self.tinseltoe_timer = randint(50, 80)
        self.tinseltoe_flag = 1

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
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
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

        # Level Font
        self.level_font = pygame.font.Font('../fonts/space_invaders.ttf', LEVEL_FONT)
        self.level_multiplier = 1
        self.level_start = 1
        self.level_start_countdown = 0

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

    # Summon Tinsletoe
    def summon_tinseltoe(self):
        self.tinseltoe_timer -= 1
        if self.tinseltoe_timer <= 0:
            self.tinseltoe.add(Tinseltoe(choice(["left", "right"])))
            self.tinseltoe_timer = randint(500, 800)

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
                        self.score_value += round(enemy.value * (1.25 ** (self.level_multiplier - 1)))
                    present.kill()
                    if self.sound:
                        self.explosion_sound.play()
                        # explosion sound?

                if pygame.sprite.spritecollide(present, self.tinseltoe, True):
                    self.score_value += round(500 * (1.25 ** (self.level_multiplier - 1)))
                    present.kill()
                    self.tinseltoe_flag = 0


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
        gameover_font = self.gameover_font.render('SANTA  PAYS  UP!', False, (0, 0, 0))
        x = SCREEN_WIDTH / 2 - gameover_font.get_width() / 2
        self.screen.blit(gameover_font, (x, 200))

    def score(self):
        score = self.font.render('Score : ' + str(self.score_value), True, (0, 0, 0))
        x = SCREEN_WIDTH / 2 - score.get_width() / 2
        self.screen.blit(score, (x, self.font_y))

        if self.score_value > self.high_score:
            self.high_score = self.score_value
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        high_score = self.lives_font.render('High Score: ' + str(self.high_score), True, (0, 0, 0))
        x = SCREEN_WIDTH - high_score.get_width()
        self.screen.blit(high_score, (x, 20))

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

    def level(self):
        level_text = self.level_font.render('LEVEL: ' + str(self.level_multiplier), True, (0, 0, 0))
        x = SCREEN_WIDTH / 2 - level_text.get_width() / 2
        self.screen.blit(level_text, (x, 200))
        timeNow = pygame.time.get_ticks()
        timeRemaining = int((self.level_start_countdown + 5950 - timeNow) / 1000)
        level_time = self.level_font.render(str(timeRemaining), True, (0, 0, 0))
        x =  SCREEN_WIDTH / 2 - level_time.get_width() / 2
        self.screen.blit(level_time, (x, 300))
        if timeNow >= self.level_start_countdown + 5950:
            self.level_start = 0
            self.enemy_create()
            self.tinseltoe_flag = 1

    def run_game(self):
        if self.level_start:
            self.bg.draw(self.screen)
            self.score()
            self.level()

        else:
            #Updates
            if not self.game_is_over:
                self.player.update()
                self.enemies.update(self.enemy_direction)
                self.tinseltoe.update()
                self.check_hit_wall()
                self.enemy_snowballs.update()
                self.check_impacts()

                if self.tinseltoe_flag:
                    self.summon_tinseltoe()

                if len(self.enemies) == 0:
                    self.game_is_over = 2
            # ReDraws
                self.bg.draw(self.screen)
                self.player.draw(self.screen)
                self.player.sprite.presents.draw(self.screen)
                self.enemies.draw(self.screen)
                self.enemy_snowballs.draw(self.screen)
                self.tinseltoe.draw(self.screen)
                self.score()
                self.display_lives()
            if self.game_is_over:
                self.bg.draw(self.screen)
                self.score()
                self.game_over()
            if self.game_is_over == 2:
                self.bg.draw(self.screen)
                self.score()
                # self.win_game()
                self.level_start = 1
                self.level_start_countdown = pygame.time.get_ticks()
                self.level_multiplier += 1
                self.enemy_direction = -1 * (1.25 ** self.level_multiplier)
                self.game_is_over = 0
