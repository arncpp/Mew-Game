import pygame
import time
from Pet import *
from Func import *
from Button import *

pygame.init()
title = "Mew Game"
pygame.display.set_caption(str(title))

pygame.display.set_icon(MyGlobals.icon)

fps = pygame.time.Clock()
button_factory = ButtonFactory()
button_food = button_factory.button_food()

button_sleep = button_factory.button_sleep()


def run_game():
    game = True
    pygame.display.set_caption(MyGlobals.cat.pet_name)
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if MyGlobals.cat.pet_death == True:
                    stats = open("stats.txt", "w")
                else:

                    stats = open("stats.txt", "w")
                    stats.writelines(str(time.time()) + "\n")
                    stats.writelines(str(int(MyGlobals.cat.pet_hunger)) + "\n")
                    stats.writelines(str(int(MyGlobals.cat.pet_sleep)) + "\n")
                    stats.writelines(MyGlobals.cat.pet_name)
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_food.action_button_click()
                    #  button_restart.action_button_click()
                    button_sleep.action_button_click()
        if not MyGlobals.cat.pet_death:
            draw_bg_lofi()
            MyGlobals.cat.hunger_loss(0.001)
            MyGlobals.cat.sleep_loss(0.01)
            print_text("food: " + str(int(MyGlobals.cat.pet_hunger)), 600, 20)
            print_text("Sleep: " + str(int(MyGlobals.cat.pet_sleep)), 600, 80)
            draw_cat_sit()
            button_food.draw("Food")
            button_sleep.draw("Sleep")
        else:
            draw_bg_lofi()
            draw_cat_dead()
            MyGlobals.display.blit(MyGlobals.menu, (250, 100))
            print_text("Your pet is dead-inside because of", 290, 150, font_size=18)
            print_text(MyGlobals.cat.death_reason, 450, 170, font_size=18)
            print_text("Close the game to restart", 330, 200, font_size=18)

        pygame.display.update()
        fps.tick(60)


but_st = Button(20, 80, 100, 38, MyGlobals.but_in, MyGlobals.but_ac, MyGlobals.but_cl, run_game)


def show_menu():
    need_input = False
    input_text = ''
    men = pygame.image.load("images\\bg\\men.jpg")
    show = True
    isempty = False
    stats = open("stats.txt", "r")
    n_time = time.time()
    stati = {'time': '', 'food': '', 'sleep': '', 'name': ''}

    for i, line in enumerate(list(stats.readlines())):
        stati[list(stati.keys())[i]] = line

    if stati['time'] == '':
        isempty = True
        stati['time'] = time.time()
    if stati['food'] == '':
        isempty = True
        stati['food'] = "100"
    if stati['sleep'] == '':
        isempty = True
        stati['sleep'] = '100'
    if stati['name'] == '':
        isempty = True
        stati['name'] = 'NoName'

    time_loss = n_time - float(stati['time'])
    food_loss = time_loss // 10
    sleep_loss = time_loss // 20
    MyGlobals.cat.set_hunger(int(stati['food']))
    MyGlobals.cat.set_sleep(int(stati['sleep']))
    MyGlobals.cat.set_hunger(max(6, MyGlobals.cat.pet_hunger - food_loss))
    MyGlobals.cat.set_sleep(max(6, MyGlobals.cat.pet_sleep - sleep_loss))
    MyGlobals.cat.set_name(stati['name'])
    if isempty:
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
                            input_text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode
                    elif event.key == pygame.K_SPACE:

                        need_input = True

            MyGlobals.display.blit(men, (0, 0))
            print_text(str(input_text), 500, 500)
            print_text("Чтобы ввести имя нажмите пробел", 200,200)

            but_st.draw("Start")
            pygame.display.update()
    else:
        run_game()


if __name__ == '__main__':
    show_menu()
# run_game()
