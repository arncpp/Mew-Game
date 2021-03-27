import pygame
from Globals import MyGlobals
from Func import print_text
import time


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
        else:
            pygame.draw.rect(MyGlobals.display, self.inactive_color, (position_x, position_y, self.width, self.height))




class Pet:
    def __init__(self, pet_health, pet_sleep, pet_happiness, pet_hunger, pet_age, pet_death):
        self.pet_health = pet_health
        self.pet_sleep = pet_sleep
        self.pet_happiness = pet_happiness
        self.pet_hunger = pet_hunger
        self.pet_age = pet_age
        self.pet_death = pet_death

    def hunger_loss(self, hunger_loss):
        self.pet_hunger -= hunger_loss

    def hunger_replenishment(self, hunger_replenishment):
        self.pet_hunger += hunger_replenishment
        
