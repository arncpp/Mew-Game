import pygame


class MyGlobals(object):
    display_width = 600
    display_height = 800
    display = pygame.display.set_mode((display_width, display_height))
    icon = pygame.image.load('images\icon.png')
    bg = pygame.image.load(r'images\bg\bg.png')
    cat_sit = [pygame.image.load(r'images\cat_sprites\sit\sit_1.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_2.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_3.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_4.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_5.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_6.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_7.png'),
               pygame.image.load(r'images\cat_sprites\sit\sit_8.png')]
    buta = pygame.image.load(r'images\butac.png')
    butn = pygame.image.load(r'images\butin.png')