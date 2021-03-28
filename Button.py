from Globals import *
from Func import *

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height

        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, position_x, position_y, message, action, num, act=None):
        mouse = pygame.mouse.get_pos()

        if position_y < mouse[1] < position_y + self.height and position_x < mouse[0] < position_x + self.width:
            pygame.draw.rect(MyGlobals.display, self.active_color, (position_x, position_y, self.width, self.height))
            print_text(message, position_x+5, position_y)
        else:
            pygame.draw.rect(MyGlobals.display, self.inactive_color, (position_x, position_y, self.width, self.height))
            print_text(message, position_x+5, position_y)
