import pygame
from Globals import MyGlobals

bg_counter = 0
img_counter = 0


def print_text(message, x, y, font_color=(0, 0, 0), font_type="images/pixelsh.ttf", font_size=25):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    MyGlobals.display.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text("Paused. Press enter to continue", 160, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
    #  pygame.clock.tick(15)






def draw_bg_lofi():
    global bg_counter
    if bg_counter == len(MyGlobals.bg_lofi) * 4:
        bg_counter = 0
    MyGlobals.display.blit(MyGlobals.bg_lofi[bg_counter // 4], (0, 0))
    bg_counter += 1


def draw_cat_sit():
    global img_counter
    if img_counter == len(MyGlobals.cat_sit) * 11:
        img_counter = 0
    MyGlobals.display.blit(MyGlobals.cat_sit[img_counter // 11], (MyGlobals.cat_x, MyGlobals.cat_y))
    img_counter += 1
