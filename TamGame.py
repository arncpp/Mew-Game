import pygame
from Func import draw_bg_menu, menu_mus, print_menu_text, print_text
from Globals import MyGlobals
from Run_game import run_game, but_st, event_in_menu
from Stats import stats_rec

pygame.init()

# ---------Настройки окна----------------
pygame.display.set_caption(MyGlobals.title)
pygame.display.set_icon(MyGlobals.icon)


# ---------Функция показа меню---------
def show_menu():
    menu_mus()
    show = True
    stats_rec()
    if MyGlobals.isempty:
        while show:
            event_in_menu()
            draw_bg_menu()
            print_text(str(MyGlobals.input_text), MyGlobals.input_text_x,
                       MyGlobals.input_text_y,
                       font_color=MyGlobals.input_text_bg,
                       font_size=MyGlobals.input_text_size)
            print_text(str(MyGlobals.input_text),
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
