import pygame
from Pet import Pet
import os

pygame.mixer.init()


class MyGlobals(object):
    # -------------Дисплей и основное----------
    display_width = 950
    display_height = 586
    display = pygame.display.set_mode((display_width, display_height))
    display_fps = 60
    font_type_text = "images/pixelsh.ttf"
    stats_file_name = "stats.txt"
    default_pos_pic = (0, 0)
    # ------------Иконка игры------------------
    icon = pygame.image.load("images/icon.png")

    # --------------Питомец-------------------
    cat_width = 230
    cat_height = 192
    cat = Pet(100, 100, 100, 100, 106, 5)
    cat_x = display_width // 8
    cat_y = display_height - cat_height
    title = "Mew Game"
    cat_hunger_loss = 0.001
    cat_sleep_loss = 0.01
    cat_health_loss = 0.003
    cat_max_stats = "100"
    default_cat_name = "Mew"
    min_stats = 6
    stats_loss_divider = 10

    # -----------Флаг isempty------------------
    isempty = False

    # ----------Загрузка спрайтов кнопок-------
    but_ac = pygame.image.load("images/button/but_inact.png")
    but_in = pygame.image.load("images/button/but_in.png")
    but_cl = pygame.image.load("images/button/but_act.png")
    gameover = pygame.image.load("images/button/button_start.png")
    menu = pygame.image.load("images/button/but_menu.png")
    menu_button = pygame.image.load("images/button/button_menu_lofi.png")

    # ---------Константы для кнопок-------------
    text_indent_btn_x = 20
    text_indent_btn_y = -5
    btn_width = 100
    btn_height = 38
    btn_x_in_game = 10
    btn_y_in_game = 40
    btn_y_indent = 50
    button_start_x = 20
    button_start_y = 80
    button_replenishment = 5
    btn_mult_y_in_game = 12.5
    btn_mult_x_in_game = 27
    btn_healt_mult_y = 2
    button_click_left = 1
    btn_health_inscription = "Heal"
    btn_sleep_inscription = "Sleep"
    btn_food_inscription = "Food"
    btn_next_inscription = "Next"
    btn_prev_inscription = "Prev"
    btn_start_inscription = "Start"

    # ----Загрузка спрайтов для анимации кота---
    cat_sit = [pygame.image.load("images/cat_sprites/sit_col/" + "sit_" +
                                 str(i) + ".png") for i in range(1, 9)]
    death = [pygame.image.load("images/cat_sprites/dead/dead_" + str(i) +
                               ".png") for i in range(1, 9)]

    # -----Загрузка спрайтов для анимации фона---
    bg_lofi = [pygame.image.load("images/bg/lofi_bg/" + str(i) +
                                 ".png") for i in range(1, 61)]
    bg_menu = [pygame.image.load("images/bg/menu_bg/" + str(i) +
                                 ".png") for i in range(1, 89)]

    # ----------Загрузка музыки и звуков----------
    bg_music = [os.path.join(d, f) for d, dirs, m_files in
                os.walk("sounds/music") for f in m_files]
    mew_1 = pygame.mixer.Sound("sounds/cat/mew_1.wav")
    mew_2 = pygame.mixer.Sound("sounds/cat/mew_2.wav")
    mrr = pygame.mixer.Sound("sounds/cat/mrr.wav")
    eat = pygame.mixer.Sound("sounds/cat/eat.mp3")
    menu_track = "sounds/Nuver Its getting late.mp3"

    # -----------Количество треков-----------------
    tracks_number = len(bg_music)
    current_track = 0

    # --------Пользовательские события-------------
    NEXT = pygame.USEREVENT + 1
    PREV = pygame.USEREVENT - 1

    # ----------Звуковые каналы--------------------
    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
    sounds_volume = 0.2
    music_volume = 0.5

    # -----------------Цвета-----------------------
    BlACK = (0, 0, 0)
    EGGPLANT = (43, 0, 92)
    PERIWINKLE = (158, 91, 172)
    DARK_PURPLE = (135, 0, 148)
    DOVE = (52, 14, 18)
    SYRUP = (108, 90, 106)

    # ----------------Конфигурация текста----------
    font_size_in_menu = 15
    text_x_in_menu = 377
    text_y_in_menu = 50
    text_x_indent_in_menu = 3
    text_y_indent_in_menu = 30
    text_x_stats = 587
    text_y_stats = 50
    text_x_indent = 5
    text_y_indent = 40
    font_size_gameover = 30
    cat_name_x_gameover = 470
    cat_name_y_gameover = 150
    cat_name_y_indent_gameover = 40
    text_x_gameover_dead = 217
    text_x_gameover_death_reason = 417
    text_x_gameover_close = 260
    main_font_size = 25
    input_text_x = 382
    input_text_indent_x = 3
    input_text_y = 110
    input_text_bg = (52, 14, 18)
    input_text_fd = (117, 65, 71)
    input_text_size = 20
    music_font_size = 10
    music_font_pos = 545
    music_text_crop_l = 1
    music_text_crop_r = -4
    input_text_crop = -1
    text_mult_y_died = 10
    text_mult_y_died_stats = 2
    text_mult_y_died_stats_3 = 3

    # -----------Конфигурация анимации--------------
    bg_lofi_deceleration = 4
    bg_menu_deceleration = 49
    cat_deceleration = 11
    cat_dead_indent_x = -5
    cat_dead_indent_y = 40
    gameover_pos = (80, 80)







