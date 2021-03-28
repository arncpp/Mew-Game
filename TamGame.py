import pygame
import time
from Pet import *
from Func import *
from Button import *

pygame.init()

pygame.display.set_caption('Mew Game')

img_counter = 0
pygame.display.set_icon(MyGlobals.icon)

cat_width = 230
cat_height = 192
cat_x = MyGlobals.display_width // 4
cat_y = MyGlobals.display_height - cat_height - 100
cat = Pet(100, 100, 100, 100, 100)

fps = pygame.time.Clock()
button_food = Button(100, 50, (0, 255, 149), (185, 18, 238))


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
    cat.set_hunger(int(stati['food']))
    cat.set_hunger(max(6, cat.pet_hunger - food_loss))

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stats = open("stats.txt", "w")
                stats.writelines(str(time.time()) + "\n")
                stats.writelines(str(int(cat.pet_hunger)))
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    action_button_click(100, 50, 100, 50, cat.hunger_replenishment(5))
        if not cat.pet_death:
            MyGlobals.display.blit(MyGlobals.bg, (0, 0))
            cat.hunger_loss(0.001)
            print_text("food: "+ str(int(cat.pet_hunger)), 450, 20)
            draw_cat_sit()
            button_food.draw(20, 20, "Food", cat.hunger_replenishment, 5)
        else:
            print_text("Your pet is dead-inside because of", 0, 50)
            print_text(cat.death_reason, 50, 100)

        pygame.display.update()
        fps.tick(60)


def draw_cat_sit():
    global img_counter
    if img_counter == len(MyGlobals.cat_sit) * 10:
        img_counter = 0
    MyGlobals.display.blit(MyGlobals.cat_sit[img_counter // 10], (cat_x, cat_y))
    img_counter += 1


def action_button_click(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()


run_game()
