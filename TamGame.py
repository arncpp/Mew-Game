import pygame
import time
from Pet import *
from Func import *
from Button import *

pygame.init()

pygame.display.set_caption('Mew Game')

pygame.display.set_icon(MyGlobals.icon)


fps = pygame.time.Clock()
button_factory = ButtonFactory()
button_food = button_factory.button_food()


def run_game():
    game = True
    stats = open("stats.txt", "r")
    n_time = time.time()
    stati = {'time': '', 'food': ''}

    for i, line in enumerate(list(stats.readlines())):
        stati[list(stati.keys())[i]] = line

    if stati['time'] == '':
        stati['time'] = time.time()
    if stati['food'] == '':
        stati['food'] = "100"
    time_loss = n_time - float(stati['time'])
    food_loss = time_loss // 10
    MyGlobals.cat.set_hunger(int(stati['food']))
    MyGlobals.cat.set_hunger(max(6, MyGlobals.cat.pet_hunger - food_loss))

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stats = open("stats.txt", "w")
                stats.writelines(str(time.time()) + "\n")
                stats.writelines(str(int(MyGlobals.cat.pet_hunger)))
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_food.action_button_click()
        if not MyGlobals.cat.pet_death:
            draw_bg_lofi()
            MyGlobals.cat.hunger_loss(0.001)
            print_text("food: " + str(int(MyGlobals.cat.pet_hunger)), 600, 20)
            draw_cat_sit()
            button_food.draw("Food")
        else:
            print_text("Your pet is dead-inside because of", 0, 50)
            print_text(MyGlobals.cat.death_reason, 50, 100)

        pygame.display.update()
        fps.tick(60)


run_game()
