from Button import *
from Stats import *

pygame.init()

title = "Mew Game"
pygame.display.set_caption(str(title))
pygame.display.set_icon(MyGlobals.icon)
fps = pygame.time.Clock()
# -------------Кнопки--------------------
button_factory = ButtonFactory()
button_food = button_factory.button_food()
button_sleep = button_factory.button_sleep()
button_next = button_factory.button_next()


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
                    stats.writelines(str(int(MyGlobals.cat.pet_happiness)) + "\n")
                    stats.writelines(MyGlobals.cat.pet_name)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and MyGlobals.cat.pet_death is not True:
                if event.button == 1:
                    button_food.action_button_click()
                    button_sleep.action_button_click()
                    button_next.action_button_click()

            elif event.type == MyGlobals.NEXT:
                next_track()

        if not MyGlobals.cat.pet_death:
            draw_bg_lofi()
            MyGlobals.cat.hunger_loss(0.001)
            MyGlobals.cat.sleep_loss(0.01)
            draw_pet_stats()
            draw_cat_sit()
            button_food.draw("Food")
            button_sleep.draw("Sleep")
            print_text(str(
                MyGlobals.bg_music[MyGlobals.current_track][
                MyGlobals.bg_music[MyGlobals.current_track].rfind("\\") + 1:-4]), 10, 545)
            button_next.draw("Next")
        else:
            draw_bg_lofi()
            draw_cat_dead()
            MyGlobals.display.blit(MyGlobals.gameover, (80, 80))
            pet_died()

        pygame.display.update()
        fps.tick(60)


# ----------Кнопка старта---------------
but_st = Button(20, 80, 100, 38, MyGlobals.menu_button, MyGlobals.but_ac, MyGlobals.but_cl, run_game)


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
            print_text(str(input_text), 380, 110, font_color=(117, 65, 71), font_size=15)
            print_text("To start typing name, press the SPACE BAR.", 380, 50, font_color=(108, 90, 106), font_size=15)
            print_text("After you finish typing, click TAB.", 380, 80, font_color=(108, 90, 106), font_size=15)

            but_st.draw("Start")
            pygame.display.update()
    else:
        run_game()


if __name__ == '__main__':
    show_menu()
