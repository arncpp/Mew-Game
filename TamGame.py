from Button import Button
from Button import ButtonFactory
from Func import draw_bg_lofi
from Func import draw_bg_menu
from Func import draw_cat_sit
from Func import draw_cat_dead
from Func import draw_pet_stats
from Func import menu_mus
from Func import next_track
from Func import pet_died
from Func import play_music
from Func import print_menu_text
from Func import print_text
from Func import prev_track
from Globals import MyGlobals
import pygame
from Stats import stats_rec
import time



pygame.init()
# ---------Настройки окна----------------
pygame.display.set_caption(MyGlobals.title)
pygame.display.set_icon(MyGlobals.icon)
fps = pygame.time.Clock()
# -------------Кнопки--------------------
button_factory = ButtonFactory()
button_food = button_factory.button_food()
button_sleep = button_factory.button_sleep()
button_health = button_factory.button_health()
button_next = button_factory.button_next()
button_prev = button_factory.button_prev()


# -----Основной цикл игры--------------
def run_game():
    play_music()
    game = True
    pygame.display.set_caption(MyGlobals.cat.pet_name)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if MyGlobals.cat.pet_death is True:
                    stats_rec.stats = open("stats.txt", "w")
                else:
                    stats = open("stats.txt", "w")
                    stats.writelines(str(time.time()) + "\n")
                    stats.writelines(str(int(MyGlobals.cat.pet_hunger)) + "\n")
                    stats.writelines(str(int(MyGlobals.cat.pet_sleep)) + "\n")
                    stats.writelines(
                        str(int(MyGlobals.cat.pet_happiness)) + "\n")
                    stats.writelines(
                        str(int(MyGlobals.cat.pet_health)) + "\n")
                    stats.writelines(MyGlobals.cat.pet_name)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    MyGlobals.cat.pet_death is not True:
                if event.button == 1:
                    button_food.action_button_click()
                    button_sleep.action_button_click()
                    button_health.action_button_click()
                    button_next.action_button_click()
                    button_prev.action_button_click()
            elif event.type == MyGlobals.NEXT:
                next_track()
            elif event.type == MyGlobals.PREV:
                prev_track()
        if not MyGlobals.cat.pet_death:
            draw_bg_lofi()
            MyGlobals.cat.hunger_loss(0.001)
            MyGlobals.cat.sleep_loss(0.01)
            MyGlobals.cat.health_loss(0.003)
            draw_pet_stats()
            draw_cat_sit()
            button_food.draw("Food", 20, -5)
            button_sleep.draw("Sleep", 20, -5)
            button_health.draw("Heal", 20, -5)
            print_text(str(
                MyGlobals.bg_music[MyGlobals.current_track][
                MyGlobals.bg_music[MyGlobals.current_track].rfind(
                    "\\") + 1:-4]), 10, 545)
            button_next.draw("Next", 20, -5)
            button_prev.draw("Prev", 20, -5)
        else:
            draw_bg_lofi()
            draw_cat_dead()
            MyGlobals.display.blit(MyGlobals.gameover, (80, 80))
            pet_died()
        pygame.display.update()
        fps.tick(60)


# ----------Кнопка старта---------------
but_st = Button(20, 80, 100, 38, MyGlobals.menu_button, MyGlobals.but_ac,
                MyGlobals.but_cl, run_game)


# --------------------------------------


# ---------Функция показа меню---------
def show_menu():
    menu_mus()
    need_input = False
    input_text = ''
    show = True
    stats_rec()
    if MyGlobals.isempty:
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        but_st.action_button_click()
                elif event.type == pygame.KEYDOWN:
                    if need_input:
                        if event.key == pygame.K_TAB:
                            need_input = False
                            MyGlobals.cat.set_name(input_text)
                            pygame.display.set_caption(MyGlobals.cat.pet_name)
                            input_text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode
                    elif event.key == pygame.K_SPACE:
                        need_input = True
            draw_bg_menu()
            print_text(str(input_text), 382, 110, font_color=(52, 14, 18),
                       font_size=20)
            print_text(str(input_text), 385, 110, font_color=(117, 65, 71),
                       font_size=20)
            print_menu_text()
            but_st.draw("Start", 20, -5)
            pygame.display.update()
    else:
        run_game()


if __name__ == '__main__':
    show_menu()
