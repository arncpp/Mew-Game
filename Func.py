# ----------Импорт--------------
import pygame
from Globals import MyGlobals
# ------------------------------

bg_counter = 0
img_counter = 0
d_counter = 0
bg_menu_counter = 0


def print_text(message, x, y, font_color=(0, 0, 0),
               font_type="images/pixelsh.ttf", font_size=25):
    '''
    Функция печати текста на экране
    :param message: сообщение, которое требуется вывести на экран
    :param x: позиция по x
    :param y: позиция по y
    :param font_color: цвет текста
    :param font_type: тип шрифта
    :param font_size: размер шрифта
    :return: ничего не возвращает
    '''
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    MyGlobals.display.blit(text, (x, y))


def draw_bg_lofi():
    '''
    Отрисовка анимации заднего фона в основной игре
    :return: ничего не возвращает
    '''
    global bg_counter
    if bg_counter == len(MyGlobals.bg_lofi) * 4:
        bg_counter = 0
    MyGlobals.display.blit(MyGlobals.bg_lofi[bg_counter // 4], (0, 0))
    bg_counter += 1


def draw_bg_menu():
    '''
    Отрисовка анимации заднего фона в меню
    :return: ничего не возвращает
    '''
    global bg_menu_counter
    if bg_menu_counter == len(MyGlobals.bg_menu) * 49:
        bg_menu_counter = 0
    MyGlobals.display.blit(MyGlobals.bg_menu[bg_menu_counter // 49], (0, 0))
    bg_menu_counter += 1


def draw_cat_sit():
    '''
    Отрисовка анимации сидящего кота
    :return: Ничего не возвращает
    '''
    global img_counter
    if img_counter == len(MyGlobals.cat_sit) * 11:
        img_counter = 0
    MyGlobals.display.blit(MyGlobals.cat_sit[img_counter // 11],
                           (MyGlobals.cat_x, MyGlobals.cat_y))
    img_counter += 1


def draw_cat_dead():
    '''
    Отрисовка анимации смерти кота
    :return: Ничего не возвращает
    '''
    global d_counter
    if d_counter == len(MyGlobals.death) * 11:
        d_counter -= 1

    MyGlobals.display.blit(MyGlobals.death[d_counter // 11],
                           (MyGlobals.cat_x - 5, MyGlobals.cat_y + 40))
    d_counter += 1


def play_music():
    '''
    Воспроизводит музыку в основной игре
    :return:
    '''
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MyGlobals.NEXT)


def menu_mus():
    '''
    Функция бесконечно играет трек в меню
    :return: ничего не возвращает
    '''
    pygame.mixer.music.load(MyGlobals.menu_track)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)


def next_track():
    '''
    Переводит на следующий трек
    :return: ничего не возвращает
    '''
    MyGlobals.current_track = (MyGlobals.current_track
                               + 1) % MyGlobals.tracks_number
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()


def prev_track():
    '''
    Переводит на предыдущий трек
    :return: ничего не возвращает
    '''
    MyGlobals.current_track = (MyGlobals.current_track
                               - 1) % MyGlobals.tracks_number
    pygame.mixer.music.load(MyGlobals.bg_music[MyGlobals.current_track])
    pygame.mixer.music.play()


def mew_1():
    '''
    Функция воспроизводит первый тип мяуканья кота в нулевом звуковом канале
    :return: ничего не возвращает
    '''
    MyGlobals.channel1.play(MyGlobals.mew_1)
    MyGlobals.mew_1.set_volume(0.2)


def mew_2():
    '''
    Функция воспроизводит второй тип мяуканя кота в нулевом звуковом канале
    :return: ничего не возвращает
    '''
    MyGlobals.channel1.play(MyGlobals.mew_2)
    MyGlobals.mew_2.set_volume(0.2)


def mrr():
    '''
    Функция воспроизводит мурлыканье кота в нулевом звуковом канале
    :return: ничего не возвращает
    '''
    MyGlobals.channel1.play(MyGlobals.mrr)
    MyGlobals.mrr.set_volume(0.2)


def eat_sound():
    '''
    Функция воспроизводит звуки еды кота в нулевом звуковом канале
    :return: ничего не возвращает
    '''
    MyGlobals.channel1.play(MyGlobals.eat)


def pet_died():
    '''
    Отрисовка 3d текста, если кот умер
    :return: ничего не возвращает
    '''
    print_text(MyGlobals.cat.pet_name,
               470 - len(MyGlobals.cat.pet_name) / 2 * 20, 150,
               font_color=(43, 0, 92),
               font_size=30)
    print_text(MyGlobals.cat.pet_name,
               475 - len(MyGlobals.cat.pet_name) / 2 * 20, 150,
               font_color=(158, 91, 172), font_size=30)
    print_text("is dead-inside because of the", 217, 190,
               font_color=(43, 0, 92), font_size=30)
    print_text("is dead-inside because of the", 222, 190,
               font_color=(158, 91, 172), font_size=30)
    print_text(MyGlobals.cat.death_reason, 417, 230, font_color=(43, 0, 92),
               font_size=30)
    print_text(MyGlobals.cat.death_reason, 422, 230, font_color=(158, 91, 172),
               font_size=30)
    print_text("Close the game to restart", 260, 270, font_color=(43, 0, 92),
               font_size=30)
    print_text("Close the game to restart", 265, 270,
               font_color=(158, 91, 172), font_size=30)


def draw_pet_stats():
    print_text("Food:  " + str(int(MyGlobals.cat.pet_hunger)), 587, 50)
    print_text("Food:  " + str(int(MyGlobals.cat.pet_hunger)), 592, 50,
               font_color=(135, 0, 148))
    print_text("Sleep: " + str(int(MyGlobals.cat.pet_sleep)), 587, 90)
    print_text("Sleep: " + str(int(MyGlobals.cat.pet_sleep)), 592, 90,
               font_color=(135, 0, 148))
    print_text("Happy: " + str(int(MyGlobals.cat.pet_happiness)), 587, 170)
    print_text("Happy: " + str(int(MyGlobals.cat.pet_happiness)), 592, 170,
               font_color=(135, 0, 148))
    print_text("Health:" + str(int(MyGlobals.cat.pet_health)), 587, 130)
    print_text("Health:" + str(int(MyGlobals.cat.pet_health)), 592, 130,
               font_color=(135, 0, 148))


def print_menu_text():
    print_text("To start typing name, press the SPACE BAR.", 377, 50,
               font_color=(52, 14, 18), font_size=15)
    print_text("To start typing name, press the SPACE BAR.", 380, 50,
               font_color=(108, 90, 106), font_size=15)
    print_text("After you finish typing, click TAB.", 377, 80,
               font_color=(52, 14, 18), font_size=15)
    print_text("After you finish typing, click TAB.", 380, 80,
               font_color=(108, 90, 106), font_size=15)
