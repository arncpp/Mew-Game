# ----------Импорт--------------
import pygame
from Pet import Pet
# ------------------------------

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
    cat = Pet(100, 100, 100, 100)
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
    bg_music = ["sounds\\music\\Joji - Modus.mp3",
                "sounds\\music\\LiL Peep - Star Shopping.mp3",
                "sounds\\music\\Powfu - Death Bed.mp3",
                "sounds\\music\\Joji - Yeah Right.mp3",
                "sounds\\music\\Petit biscuit - sunset lover.mp3",
                "sounds\\music\\The Neighbourhood - Daddy Issues.mp3",
                "sounds\\music\\Tommee Profitt - In The End.mp3",
                "sounds\\music\\Bazzi - Fantasy.mp3",
                "sounds\\music\\Arctic Monkeys - Do I Wanna Know.mp3",
                "sounds\\music\\The Neighbourhood - Sweater Weather.mp3",
                "sounds\\music\\Кит ты маму мав.mp3",
                "sounds\\music\\Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
                "sounds\\music\\White Town - Your Woman.mp3",
                "sounds\\music\\The White Stripes - Seven Nation Army.mp3",
                "sounds\\music\\The Neighbourhood - Afraid.mp3",
                "sounds\\music\\Palaye Royale - Lonely.mp3",
                "sounds\\music\\Mr.kitty - After dark.mp3",
                "sounds\\music\\Lilly Wood & Robin Schulz - Prayer In C.mp3",
                "sounds\\music\\Lil Peep - Benz Truck.mp3",
                "sounds\\music\\Lana Del Rey - Summertime Sadness.mp3",
                "sounds\\music\\Jaymes Young - Infinity.mp3",
                "sounds\\music\\Bob Dylan - Knockin' On Heaven's Door.mp3",
                "sounds\\music\\grandson - Blood Water.mp3",
                "sounds\\music\\Gorillaz - Feel Good Inc.mp3",
                "sounds\\music\\Gorillaz - Dirty Harry.mp3",
                "sounds\\music\\Chris Isaak - Wicked Game.mp3",
                "sounds\\music\\Brennan Savage - Look At Me Now.mp3",
                "sounds\\music\\Blue Foundation - Eyes On Fire.mp3", ]
    mew_1 = pygame.mixer.Sound("sounds\\cat\\mew_1.wav")
    mew_2 = pygame.mixer.Sound("sounds\\cat\\mew_2.wav")
    mrr = pygame.mixer.Sound("sounds\\cat\\mrr.wav")
    eat = pygame.mixer.Sound("sounds\\cat\\eat.mp3")
    menu_track = "sounds\\music\\Nuver Its getting late.mp3"
    # -----------Количество треков-----------------
    tracks_number = len(bg_music)
    current_track = 0
    # --------Пользовательские события-------------
    NEXT = pygame.USEREVENT + 1
    PREV = pygame.USEREVENT - 1
    # ----------Звуковые каналы--------------------
    channel1 = pygame.mixer.Channel(0)
    channel2 = pygame.mixer.Channel(1)
