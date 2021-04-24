import pygame

from Globals import MyGlobals

pygame.mixer.init()

# ------Счётчики спрайтов-------------
bg_counter = 0
img_counter = 0
d_counter = 0
bg_menu_counter = 0


def print_text(message, x, y, font_color=MyGlobals.BlACK,
               font_type=MyGlobals.font_type_text,
               font_size=MyGlobals.main_font_size):
    """
    Функция печати текста на экране
    :param message: сообщение, которое требуется вывести на экран
    :param x: позиция по x
    :param y: позиция по y
    :param font_color: цвет текста
    :param font_type: тип шрифта
    :param font_size: размер шрифта
    """
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    MyGlobals.display.blit(text, (x, y))


def draw_bg_lofi():
    """
    Отрисовка анимации заднего фона в основной игре
    """
    global bg_counter
    if bg_counter == len(MyGlobals.bg_lofi) * MyGlobals.bg_lofi_deceleration:
        bg_counter = 0
    MyGlobals.display.blit(
        MyGlobals.bg_lofi[bg_counter // MyGlobals.bg_lofi_deceleration],
        MyGlobals.default_pos_pic)
    bg_counter += 1


def draw_bg_menu():
    """
    Отрисовка анимации заднего фона в меню
    """
    global bg_menu_counter
    if bg_menu_counter == len(MyGlobals.bg_menu) * \
            MyGlobals.bg_menu_deceleration:
        bg_menu_counter = 0
    MyGlobals.display.blit(
        MyGlobals.bg_menu[bg_menu_counter // MyGlobals.bg_menu_deceleration],
        MyGlobals.default_pos_pic)
    bg_menu_counter += 1


def draw_cat_sit():
    """
    Отрисовка анимации сидящего кота
    """
    global img_counter
    if img_counter == len(MyGlobals.cat_sit) * MyGlobals.cat_deceleration:
        img_counter = 0
    MyGlobals.display.blit(
        MyGlobals.cat_sit[img_counter // MyGlobals.cat_deceleration],
        (MyGlobals.cat_x, MyGlobals.cat_y))
    img_counter += 1


def draw_cat_dead():
    """
    Отрисовка анимации смерти кота
    """
    global d_counter
    if d_counter == len(MyGlobals.death) * MyGlobals.cat_deceleration:
        d_counter -= 1

    MyGlobals.display.blit(
        MyGlobals.death[d_counter // MyGlobals.cat_deceleration],
        (MyGlobals.cat_x + MyGlobals.cat_dead_indent_x,
         MyGlobals.cat_y + MyGlobals.cat_dead_indent_y))
    d_counter += 1


def play_music():
    """
    Воспроизводит музыку в основной игре
    """
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MyGlobals.NEXT)


def menu_mus():
    """
    Функция бесконечно играет трек в меню
    """
    pygame.mixer.music.load(MyGlobals.menu_track)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(MyGlobals.music_volume)


def next_track():
    """
    Переводит на следующий трек
    """
    MyGlobals.current_track = (MyGlobals.current_track
                               + 1) % MyGlobals.tracks_number
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()


def prev_track():
    """
    Переводит на предыдущий трек
    """
    MyGlobals.current_track = (MyGlobals.current_track
                               - 1) % MyGlobals.tracks_number
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()


def mew_1():
    """
    Функция воспроизводит первый тип мяуканья кота в нулевом звуковом канале
    """
    pygame.mixer.Channel(MyGlobals.channel1).play(
        pygame.mixer.Sound(MyGlobals.mew_1))
    pygame.mixer.Sound(MyGlobals.mew_1).set_volume(MyGlobals.sounds_volume)


def mew_2():
    """
    Функция воспроизводит второй тип мяуканья кота в нулевом звуковом канале
    """
    pygame.mixer.Channel(MyGlobals.channel1).play(
        pygame.mixer.Sound(MyGlobals.mew_2))
    pygame.mixer.Sound(MyGlobals.mew_2).set_volume(MyGlobals.sounds_volume)


def mrr():
    """
    Функция воспроизводит мурлыканье кота в нулевом звуковом канале
    """
    pygame.mixer.Channel(MyGlobals.channel1).play(
        pygame.mixer.Sound(MyGlobals.mrr))
    pygame.mixer.Sound(MyGlobals.mrr).set_volume(MyGlobals.sounds_volume)


def eat_sound():
    '''
    Функция воспроизводит звуки еды кота в нулевом звуковом канале
    '''
    pygame.mixer.Channel(MyGlobals.channel1).play(
        pygame.mixer.Sound(MyGlobals.eat))


def pet_died():
    """
    Отрисовка 3d текста, если кот умер
    """
    print_text(MyGlobals.cat.get_pet_name(),
               MyGlobals.cat_name_x_gameover - len(
                   MyGlobals.cat.get_pet_name()) * MyGlobals.text_mult_y_died,
               MyGlobals.cat_name_y_gameover,
               font_color=MyGlobals.EGGPLANT,
               font_size=MyGlobals.font_size_gameover)
    print_text(MyGlobals.cat.get_pet_name(),
               MyGlobals.text_x_indent + MyGlobals.cat_name_x_gameover
               - len(MyGlobals.cat.get_pet_name()) *
               MyGlobals.text_mult_y_died,
               MyGlobals.cat_name_y_gameover,
               font_color=MyGlobals.PERIWINKLE,
               font_size=MyGlobals.font_size_gameover)
    print_text("is dead-inside because of the", MyGlobals.text_x_gameover_dead,
               MyGlobals.cat_name_y_gameover +
               MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.EGGPLANT,
               font_size=MyGlobals.font_size_gameover)
    print_text("is dead-inside because of the",
               MyGlobals.text_x_gameover_dead + MyGlobals.text_x_indent,
               MyGlobals.cat_name_y_gameover +
               MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.PERIWINKLE,
               font_size=MyGlobals.font_size_gameover)
    print_text(MyGlobals.cat.death_reason,
               MyGlobals.text_x_gameover_death_reason,
               MyGlobals.cat_name_y_gameover +
               MyGlobals.text_mult_y_died_stats *
               MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.EGGPLANT,
               font_size=MyGlobals.font_size_gameover)
    print_text(MyGlobals.cat.death_reason,
               MyGlobals.text_x_gameover_death_reason +
               MyGlobals.text_x_indent,
               MyGlobals.cat_name_y_gameover +
               MyGlobals.text_mult_y_died_stats *
               MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.PERIWINKLE,
               font_size=MyGlobals.font_size_gameover)
    print_text("Close the game to restart", MyGlobals.text_x_gameover_close,
               MyGlobals.cat_name_y_gameover +
               3 * MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.EGGPLANT,
               font_size=MyGlobals.font_size_gameover)
    print_text("Close the game to restart",
               MyGlobals.text_x_gameover_close + MyGlobals.text_x_indent,
               MyGlobals.cat_name_y_gameover +
               3 * MyGlobals.cat_name_y_indent_gameover,
               font_color=MyGlobals.PERIWINKLE,
               font_size=MyGlobals.font_size_gameover)


def draw_pet_stats():
    """
    Отрисовка статистики кота
    """
    print_text(f"Food:  {int(MyGlobals.cat.get_pet_hunger())}",
               MyGlobals.text_x_stats, MyGlobals.text_y_stats)
    print_text(f"Food:  {int(MyGlobals.cat.get_pet_hunger())}",
               MyGlobals.text_x_stats + MyGlobals.text_x_indent,
               MyGlobals.text_y_stats,
               font_color=MyGlobals.DARK_PURPLE)
    print_text(f"Sleep: {int(MyGlobals.cat.get_pet_sleep())}",
               MyGlobals.text_x_stats,
               MyGlobals.text_y_stats + MyGlobals.text_y_indent)
    print_text(f"Sleep: {int(MyGlobals.cat.get_pet_sleep())}",
               MyGlobals.text_x_stats + MyGlobals.text_x_indent,
               MyGlobals.text_y_stats + MyGlobals.text_y_indent,
               font_color=MyGlobals.DARK_PURPLE)
    print_text(f"Happy: {int(MyGlobals.cat.get_pet_happiness())}",
               MyGlobals.text_x_stats,
               MyGlobals.text_y_stats + MyGlobals.text_mult_y_died_stats_3 *
               MyGlobals.text_y_indent)
    print_text(f"Happy: {int(MyGlobals.cat.get_pet_happiness())}",
               MyGlobals.text_x_stats + MyGlobals.text_x_indent,
               MyGlobals.text_y_stats + MyGlobals.text_mult_y_died_stats_3 *
               MyGlobals.text_y_indent, font_color=MyGlobals.DARK_PURPLE)
    print_text(f"Health: {int(MyGlobals.cat.get_pet_health())}",
               MyGlobals.text_x_stats,
               MyGlobals.text_y_stats + MyGlobals.text_mult_y_died_stats *
               MyGlobals.text_y_indent)
    print_text(f"Health: {int(MyGlobals.cat.get_pet_health())}",
               MyGlobals.text_x_stats + MyGlobals.text_x_indent,
               MyGlobals.text_y_stats + MyGlobals.text_mult_y_died_stats *
               MyGlobals.text_y_indent,
               font_color=MyGlobals.DARK_PURPLE)


def print_menu_text():
    """
    Отрисовка инструкций в главном меню
    """
    print_text("To start typing name, press the SPACE BAR.",
               MyGlobals.text_x_in_menu, MyGlobals.text_y_in_menu,
               font_color=MyGlobals.DOVE,
               font_size=MyGlobals.font_size_in_menu)
    print_text("To start typing name, press the SPACE BAR.",
               MyGlobals.text_x_in_menu + MyGlobals.text_x_indent_in_menu,
               MyGlobals.text_y_in_menu,
               font_color=MyGlobals.SYRUP,
               font_size=MyGlobals.font_size_in_menu)
    print_text("After you finish typing, click TAB.", MyGlobals.text_x_in_menu,
               MyGlobals.text_y_in_menu + MyGlobals.text_y_indent_in_menu,
               font_color=MyGlobals.DOVE,
               font_size=MyGlobals.font_size_in_menu)
    print_text("After you finish typing, click TAB.",
               MyGlobals.text_x_in_menu + MyGlobals.text_x_indent_in_menu,
               MyGlobals.text_y_in_menu + MyGlobals.text_y_indent_in_menu,
               font_color=MyGlobals.SYRUP,
               font_size=MyGlobals.font_size_in_menu)
