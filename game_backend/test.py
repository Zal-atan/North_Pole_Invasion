import pygame
from variables import *

gameover_font = pygame.font.Font('../fonts/space_invaders.ttf', GAME_OVER_FONT)

def game_over():
    gameover_font = gameover_font.render('GAME OVER', True, (0, 0, 0))
    self.screen.blit(gameover_font, (200, 200))
