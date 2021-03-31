import pygame
from Pet import Pet
import os

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
    cat = Pet(100, 100, 100, 100, 106, 5)
    cat_x = display_width // 8
    cat_y = display_height - cat_height
    title = "Mew Game"

    # -----------Флаг isempty------------------
    isempty = False

    # ----------Загрузка спрайтов кнопок-------
    but_ac = pygame.image.load("images\\button\\but_inact.png")
    but_in = pygame.image.load("images\\button\\but_in.png")
    but_cl = pygame.image.load("images\\button\\but_act.png")
    gameover = pygame.image.load("images\\button\\button_start.png")
    menu = pygame.image.load("images\\button\\but_menu.png")
    menu_button = pygame.image.load("images\\button\\button_menu_lofi.png")

    # -----Отступы для текста на кнопке---------
    text_indent_btn_x = 20
    text_indent_btn_y = -5

    # ----Загрузка спрайтов для анимации кота---
    cat_sit = [pygame.image.load(
        "images\\cat_sprites\\sit_col\\" + "sit_" + str(i) + ".png") for i in
        range(1, 9)]
    death = [
        pygame.image.load("images\\cat_sprites\\dead\\dead_" + str(i) + ".png")
        for i in range(1, 9)]

    # -----Загрузка спрайтов для анимации фона---
    bg_lofi = [pygame.image.load("images\\bg\\lofi_bg\\"
                                 + str(i) + ".png") for i in range(1, 61)]
    bg_menu = [pygame.image.load("images\\bg\\menu_bg\\" + str(i) + ".png") for
               i in range(1, 89)]

    # ----------Загрузка музыки и звуков----------
    bg_music = [os.path.join(d, f) for d, dirs, m_files in
                os.walk("sounds\\music") for f in m_files]
    mew_1 = pygame.mixer.Sound("sounds\\cat\\mew_1.wav")
    mew_2 = pygame.mixer.Sound("sounds\\cat\\mew_2.wav")
    mrr = pygame.mixer.Sound("sounds\\cat\\mrr.wav")
    eat = pygame.mixer.Sound("sounds\\cat\\eat.mp3")
    menu_track = "sounds\\Nuver Its getting late.mp3"

    # -----------Количество треков-----------------
    tracks_number = len(bg_music)
    current_track = 0

    # --------Пользовательские события-------------
    NEXT = pygame.USEREVENT + 1
    PREV = pygame.USEREVENT - 1

    # ----------Звуковые каналы--------------------
    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
