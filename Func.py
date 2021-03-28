import pygame
from Globals import MyGlobals


def print_text(message, x, y, font_color=(0, 0, 0), font_type="images/pixelsh.ttf", font_size=30):
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
