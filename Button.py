from Globals import MyGlobals
from Func import *
from Pet import *


class Button:
    def __init__(self, position_x, position_y, width, height, inactive_color, active_color, click_im, action, num=None):
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.click_im = click_im
        self.action = action
        self.num = num

    def draw(self, message):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.position_y < mouse[1] < self.position_y + self.height and self.position_x < mouse[
            0] < self.position_x + self.width:
            if click[0] == 1 and self.action != None:
                MyGlobals.display.blit(self.click_im, (self.position_x, self.position_y))
                print_text(message, self.position_x + 20, self.position_y)
            else:
                MyGlobals.display.blit(self.active_color, (self.position_x, self.position_y))
                print_text(message, self.position_x + 20, self.position_y - 5)

        else:
            MyGlobals.display.blit(self.inactive_color, (self.position_x, self.position_y))
            print_text(message, self.position_x + 20, self.position_y - 5)

    def action_button_click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.position_x < mouse[0] < self.position_x + self.width and self.position_y < mouse[
            1] < self.position_y + self.height:
            if click[0] == 1 and self.action != None:
                if self.num != None:
                    self.action(self.num)
                else:
                    self.action()


class ButtonFactory:
    def button_food(self):
        return Button(20, 40, 100, 38, MyGlobals.but_in, MyGlobals.but_ac, MyGlobals.but_cl,
                      MyGlobals.cat.hunger_replenishment, 5)

    def button_sleep(self):
        return Button(20, 80, 100, 38, MyGlobals.but_in, MyGlobals.but_ac, MyGlobals.but_cl,
                      MyGlobals.cat.sleep_replenishment, 5)
