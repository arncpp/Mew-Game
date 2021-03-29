import pygame
from Pet import *
import time

pygame.mixer.init()


class MyGlobals(object):
    # --------------Дисплей-------------------
    display_width = 950
    display_height = 586
    display = pygame.display.set_mode((display_width, display_height))
    # ------------Иконка игры------------------
    icon = pygame.image.load('images\icon.png')
    # --------------Питомец-------------------
    cat_width = 230
    cat_height = 192
    cat = Pet(100, 100, 100, 100, 100)
    cat_x = display_width // 8
    cat_y = display_height - cat_height
    # -----------Флаг isempty------------------
    isempty = False
    # ----------Загрузка спрайтов кнопок-------
    but_ac = pygame.image.load("images\\button\\but_inact.png")
    but_in = pygame.image.load("images\\button\\but_in.png")
    but_cl = pygame.image.load("images\\button\\but_act.png")
    gameover = pygame.image.load("images\\button\\button_start.png")
    menu = pygame.image.load("images\\button\\but_menu.png")
    menu_button = pygame.image.load("images\\button\\button_menu_lofi.png")
    # ----Загрузка спрайтов для анимации кота---
    cat_sit = [pygame.image.load("images\\cat_sprites\\sit_col\\" + "sit_" + str(i) + ".png") for i in range(1, 9)]
    death = [pygame.image.load("images\\cat_sprites\\dead\\dead_" + str(i) + ".png") for i in range(1, 9)]
    # -----Загрузка спрайтов для анимации фона---
    bg_lofi = [pygame.image.load("images\\bg\\lofi_bg\\" + str(i) + ".png") for i in range(1, 61)]
    bg_menu = [pygame.image.load("images\\bg\\menu_bg\\" + str(i) + ".png") for i in range(1, 89)]
    # ----------Загрузка музыки и звуков----------
    bg_music = ["sounds\\music\\Joji - Modus.wav", "sounds\\music\\LiL Peep - Star Shopping.wav",
                "sounds\\music\\Powfu - Death Bed.wav", "sounds\\music\\Joji - Yeah Right.wav",
                "sounds\\music\\Petit biscuit - sunset lover.wav",
                "sounds\\music\\The Neighbourhood - Daddy Issues.wav",
                "sounds\\music\\Tommee Profitt - In The End.wav", "sounds\\music\\Bazzi - Fantasy.wav",
                "sounds\\music\\Arctic Monkeys - Do I Wanna Know.wav",
                "sounds\\music\\The Neighbourhood - Sweater Weather.wav", "sounds\\music\\Кит ты маму мав.wav",
                "sounds\\music\\Arctic Monkeys - Why'd You Only Call Me When You're High.wav"]
    mew_1 = pygame.mixer.Sound("sounds\\cat\\mew_1.wav")
    mew_2 = pygame.mixer.Sound("sounds\\cat\\mew_2.wav")
    mrr = pygame.mixer.Sound("sounds\\cat\\mrr.wav")
    menu_track = "sounds\\music\\Nuver Its getting late.wav"

    # -----------Количество треков-----------------
    tracks_number = len(bg_music)
    current_track = 0
    # --------Пользовательские события-------------
    NEXT = pygame.USEREVENT + 1
    # ----------Звуковые каналы--------------------
    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
