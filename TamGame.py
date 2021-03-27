import pygame
import time
from Classes import *
from Globals import MyGlobals

pygame.init()

pygame.display.set_caption('Mew Game')

icon = pygame.image.load('images\icon.png')
bg = pygame.image.load(r'images\bg\bg.png')
cat_sit = [pygame.image.load(r'images\cat_sprites\sit\sit_1.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_2.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_3.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_4.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_5.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_6.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_7.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_8.png')]
img_counter = 0
pygame.display.set_icon(icon)

cat_width = 230
cat_height = 192
cat_x = MyGlobals.display_width // 4
cat_y = MyGlobals.display_height - cat_height - 100
cat = Pet(100, 100, 100, 100, 100, False)

fps = pygame.time.Clock()
button = Button(100, 100, (0, 24, 5), (186, 250, 90))


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    action_button_click(100, 50, 100, 50, cat.hunger_replenishment(5))

        MyGlobals.display.blit(bg, (0, 0))
        cat.hunger_loss(0.001)
        print_text(str(int(cat.pet_hunger)), 500, 500)
        draw_cat_sit()
        button.draw(100, 50, "b", cat.hunger_replenishment, 5)

        pygame.display.update()
        fps.tick(60)


def draw_cat_sit():
    global img_counter
    if img_counter == len(cat_sit) * 10:
        img_counter = 0
    MyGlobals.display.blit(cat_sit[img_counter // 10], (cat_x, cat_y))
    img_counter += 1


def action_button_click(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()


run_game()
