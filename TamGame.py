import pygame

pygame.init()

display_width = 600
display_height = 800

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Mew Game')

icon = pygame.image.load('images\icon.png')
bg = pygame.image.load(r'images\bg\bg.png')
cat_sit = [pygame.image.load(r'images\cat_sprites\sit\sit_1.png'), pygame.image.load(r'images\cat_sprites\sit\sit_2.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_3.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_4.png'), pygame.image.load(r'images\cat_sprites\sit\sit_5.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_6.png'),
           pygame.image.load(r'images\cat_sprites\sit\sit_7.png'), pygame.image.load(r'images\cat_sprites\sit\sit_8.png')]
img_counter = 0
pygame.display.set_icon(icon)

cat_width = 230
cat_height = 192
cat_x = display_width // 4
cat_y = display_height - cat_height - 100

fps = pygame.time.Clock()


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            display.blit(bg, (0, 0))

            draw_cat_sit()
            pygame.display.update()
            fps.tick(60)


def draw_cat_sit():
    global img_counter
    if img_counter == len(cat_sit) * 10 :
        img_counter = 0
    display.blit(cat_sit[img_counter // 10], (cat_x, cat_y))
    img_counter += 1


run_game()
