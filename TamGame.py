import pygame
import time
from Button import Button, ButtonFactory
from Func import draw_bg_lofi, draw_bg_menu, draw_cat_sit, draw_cat_dead, \
    draw_pet_stats, menu_mus, next_track, pet_died, play_music, \
    print_menu_text, print_text, prev_track
from Globals import MyGlobals
from Stats import stats_rec

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
    pygame.display.set_caption(MyGlobals.cat.get_pet_name())
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if MyGlobals.cat.pet_death is True:
                    with open(MyGlobals.stats_file_name, "w") \
                            as stats_rec.stats:
                        pass
                else:
                    with open(MyGlobals.stats_file_name, "w") as stats:
                        stats.writelines(str(time.time()) + "\n")
                        stats.writelines(
                            str(int(MyGlobals.cat.get_pet_hunger())) + "\n")
                        stats.writelines(
                            str(int(MyGlobals.cat.get_pet_sleep())) + "\n")
                        stats.writelines(
                            str(int(MyGlobals.cat.get_pet_happiness())) + "\n")
                        stats.writelines(
                            str(int(MyGlobals.cat.get_pet_health())) + "\n")
                        stats.writelines(MyGlobals.cat.get_pet_name())
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    MyGlobals.cat.pet_death is not True:
                if event.button == MyGlobals.button_click_left:
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
            MyGlobals.cat.hunger_loss(MyGlobals.cat_hunger_loss)
            MyGlobals.cat.sleep_loss(MyGlobals.cat_sleep_loss)
            MyGlobals.cat.health_loss(MyGlobals.cat_health_loss)
            draw_pet_stats()
            draw_cat_sit()
            button_food.draw(MyGlobals.btn_food_inscription)
            button_sleep.draw(MyGlobals.btn_sleep_inscription)
            button_health.draw(MyGlobals.btn_health_inscription)
            print_text(str(MyGlobals.bg_music[MyGlobals.current_track]
                           [MyGlobals.bg_music
                            [MyGlobals.current_track].rfind("\\") +
                            MyGlobals.music_text_crop_l:MyGlobals.music_text_crop_r]),
                       MyGlobals.music_font_size,
                       MyGlobals.music_font_pos)
            button_next.draw(MyGlobals.btn_next_inscription)
            button_prev.draw(MyGlobals.btn_prev_inscription)
        else:
            draw_bg_lofi()
            draw_cat_dead()
            MyGlobals.display.blit(MyGlobals.gameover, MyGlobals.gameover_pos)
            pet_died()
        pygame.display.update()
        fps.tick(MyGlobals.display_fps)


# ----------Кнопка старта---------------
but_st = Button(MyGlobals.button_start_x, MyGlobals.button_start_y,
                MyGlobals.btn_width, MyGlobals.btn_height,
                MyGlobals.menu_button, MyGlobals.but_ac,
                MyGlobals.but_cl, run_game)


# ---------Функция показа меню---------
def show_menu():
    menu_mus()
    need_input = False
    input_text = ""
    show = True
    stats_rec()
    if MyGlobals.isempty:
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == MyGlobals.button_click_left:
                    but_st.action_button_click()
                elif event.type == pygame.KEYDOWN:
                    if need_input:
                        if event.key == pygame.K_TAB:
                            need_input = False
                            MyGlobals.cat.set_name(input_text)
                            pygame.display.set_caption(
                                MyGlobals.cat.get_pet_name())
                            input_text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:MyGlobals.input_text_crop]
                        else:
                            input_text += event.unicode
                    elif event.key == pygame.K_SPACE:
                        need_input = True
            draw_bg_menu()
            print_text(str(input_text), MyGlobals.input_text_x,
                       MyGlobals.input_text_y,
                       font_color=MyGlobals.input_text_bg,
                       font_size=MyGlobals.input_text_size)
            print_text(str(input_text),
                       MyGlobals.input_text_x + MyGlobals.input_text_indent_x,
                       MyGlobals.input_text_y,
                       font_color=MyGlobals.input_text_fd,
                       font_size=MyGlobals.input_text_size)
            print_menu_text()
            but_st.draw(MyGlobals.btn_start_inscription)
            pygame.display.update()
    else:
        run_game()


if __name__ == "__main__":
    show_menu()
