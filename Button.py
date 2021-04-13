from Func import eat_sound, mrr, mew_1, mew_2, next_track, print_text, \
    prev_track
from Globals import MyGlobals
import pygame


class Button:
    def __init__(self, position_x, position_y, width, height, inactive_color,
                 active_color, click_im,
                 action, sound=None, num=None):
        '''
        :param position_x: позиция по x
        :param position_y: позиция по y
        :param width: длина кнопки
        :param height: высота кнопки
        :param inactive_color: спрайт кнопки, когда на неё не наведен курсор
        :param active_color: спрайт кнопки, когда на неё наведен курсор
        :param click_im: спрайт кнопки, когда на неё нажимают
        :param action: функция, которая выполняется при нажатии
        :param sound: звук, который издается при нажатии
        :param num: если функция(action) принимает num
        '''
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.click_im = click_im
        self.action = action
        self.num = num
        self.sound = sound

    def draw(self, message):
        '''
        Рисует кнопку на экране
        Если мышка не наведена на кнопку, то используется inactive_color
        Если наведена, то кнопка меняет цвет на active_color
        При нажатии на кнопку используется click_im
        :param message: принимает сообщение, которое требуется вывести на кнопку
        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.position_y < mouse[1] < self.position_y + self.height \
                and self.position_x < mouse[0] < self.position_x + self.width:
            if click[0] == 1 and self.action != None:
                MyGlobals.display.blit(self.click_im,
                                       (self.position_x, self.position_y))
                print_text(message,
                           self.position_x + MyGlobals.text_indent_btn_x,
                           self.position_y)
            else:
                MyGlobals.display.blit(self.active_color,
                                       (self.position_x, self.position_y))
                print_text(message,
                           self.position_x + MyGlobals.text_indent_btn_x,
                           self.position_y + MyGlobals.text_indent_btn_y)

        else:
            MyGlobals.display.blit(self.inactive_color,
                                   (self.position_x, self.position_y))
            print_text(message, self.position_x + MyGlobals.text_indent_btn_x,
                       self.position_y + MyGlobals.text_indent_btn_y)

    def action_button_click(self):
        '''
        Функция, которая регистрирует нажатия на кнопку и выполняет действие,
        которое было передано в класс кнопки
        '''
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if self.position_x < mouse[0] < self.position_x + self.width and \
                self.position_y < mouse[1] < self.position_y + self.height:
            if click[0] == 1 and self.action is not None:
                if self.num is not None:
                    self.action(self.num)
                else:
                    self.action()
                if self.sound is not None:
                    self.sound()


# паттерн фабричный метод (фабрика)
class ButtonFactory:
    def button_food(self):
        '''
        Кнопка еды, при нажатии на неё выполняется прибавление
        показателей к насыщенности питомца
        :return: возвращает кнопку, которая выполняет функцию
        hunger_replenishment(прибавляет 5 единиц еды)
        '''
        return Button(MyGlobals.btn_x_in_game, MyGlobals.btn_y_in_game,
                      MyGlobals.btn_width,
                      MyGlobals.btn_height,
                      MyGlobals.but_in, MyGlobals.but_ac,
                      MyGlobals.but_cl,
                      MyGlobals.cat.hunger_replenishment, eat_sound, 5)

    def button_sleep(self):
        '''
        Кнопка сна, при нажатии на неё выполняется прибавление ко сну питомца
        :return: возвращает кнопку, которая выполняет функцию
        sleep_replenishment(прибавляет 5 единиц сна)
        '''
        return Button(MyGlobals.btn_x_in_game,
                      MyGlobals.btn_y_in_game + MyGlobals.btn_y_indent,
                      MyGlobals.btn_width,
                      MyGlobals.btn_height,
                      MyGlobals.but_in, MyGlobals.but_ac,
                      MyGlobals.but_cl,
                      MyGlobals.cat.sleep_replenishment, mew_1, 5)

    def button_health(self):
        '''
        Кнопка здоровья, при нажатии на неё выполняется прибавление ко здоровью
        питомца
        :return: возвращает кнопку, которая выполняет функцию
        health_replenishment(прибавляет 5 единиц здоровья)
        '''
        return Button(MyGlobals.btn_x_in_game,
                      MyGlobals.btn_y_in_game + 2 * MyGlobals.btn_y_indent,
                      MyGlobals.btn_width,
                      MyGlobals.btn_height,
                      MyGlobals.but_in, MyGlobals.but_ac,
                      MyGlobals.but_cl,
                      MyGlobals.cat.health_replenishment, mew_2, 5)

    def button_next(self):
        '''
        Кнопка переключения музыки, при нажатии
        воспроизводится следующая композиция
        :return: возвращает кнопку, которая выполняет
        функцию next_track (переходит на след. трек)
        '''
        return Button(27 * MyGlobals.btn_x_in_game,
                      12.5 * MyGlobals.btn_y_in_game, MyGlobals.btn_width,
                      MyGlobals.btn_height,
                      MyGlobals.but_in, MyGlobals.but_ac,
                      MyGlobals.but_cl,
                      next_track, mrr)

    def button_prev(self):
        '''
        Кнопка переключения музыки, при нажатии
        воспроизводится следующая композиция
        :return: возвращает кнопку, которая выполняет
        функцию next_track (переходит на след. трек)
        '''
        return Button(MyGlobals.btn_x_in_game, 12.5 * MyGlobals.btn_y_in_game,
                      MyGlobals.btn_width, MyGlobals.btn_height,
                      MyGlobals.but_in, MyGlobals.but_ac,
                      MyGlobals.but_cl,
                      prev_track, mrr)
