import pygame
from Pet import *


class MyGlobals(object):
    display_width = 950
    display_height = 586
    cat_width = 230
    cat_height = 192
    cat = Pet(100, 100, 100, 100, 100)
    cat_x = display_width // 8
    cat_y = display_height - cat_height
    but_ac = pygame.image.load("images\\button\\but_inact.png")
    but_in = pygame.image.load("images\\button\\but_in.png")
    but_cl = pygame.image.load("images\\button\\but_act.png")
    menu = pygame.image.load("images\\button\\but_menu.png")
    display = pygame.display.set_mode((display_width, display_height))
    icon = pygame.image.load('images\icon.png')
    # bg = pygame.image.load(r'images\bg\lofi bg\1.png')
    cat_sit = [pygame.image.load("images\\cat_sprites\\sit_col\\" + "sit_" + str(i) + ".png") for i in range(1, 9)]
    bg_lofi = [pygame.image.load("images\\bg\\lofi_bg\\" + str(i) + ".png") for i in range(1, 61)]

    death = [pygame.image.load("images\\cat_sprites\\dead\\dead_" + str(i) + ".png") for i in range(1, 9)]
