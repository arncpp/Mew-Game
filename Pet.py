# -------Класс питомец--------------
class Pet:
    def __init__(self, pet_health, pet_sleep, pet_happiness, pet_hunger, pet_age):
        self.pet_health = pet_health
        self.pet_sleep = pet_sleep
        self.pet_happiness = pet_happiness
        self.pet_hunger = pet_hunger
        self.pet_age = pet_age
        self.pet_death = False
        self.death_reason = ''
        self.pet_name = ''

    def pet_hapiness_loss(self, pet_hapiness_loss):
        '''
        Принимает pet_hapiness_loss
        :param pet_hapiness_loss:то, что вычитается из pet_happiness
        :return: ничего не возвращает
        '''
        self.pet_happiness -= pet_hapiness_loss
        if self.pet_happiness <= 5:
            self.pet_death = True
            self.death_reason = "Sadness"

    def pet_hapiness_replenishment(self, hap_replenishment):
        '''
        Принимает hap_replenishment
        :param hap_replenishment:то, что прибавляется к pet_happiness
        :return: ничего не возвращает
        '''
        self.pet_happiness += hap_replenishment
        if self.pet_happiness >= 106:
            self.pet_happiness = 106

    def hunger_loss(self, hunger_loss):
        '''
        Принимает hunger_loss
        :param hunger_loss:то, что вычитается из pet_hunger
        :return: ничего не возвращает
        '''
        self.pet_hunger -= hunger_loss
        self.pet_hapiness_loss(0.002)
        if self.pet_hunger <= 5 or self.pet_hunger >= 105:
            self.pet_death = True
            self.death_reason = 'Food'

    def hunger_replenishment(self, hunger_replenishment):
        '''
        Принимает hunger_replenishment
        :param hunger_replenishment:то, что прибавляется к pet_hunger
        :return: ничего не возвращает
        '''
        self.pet_hunger += hunger_replenishment
        self.pet_hapiness_replenishment(3)
        if self.pet_hunger >= 106:
            self.pet_death = True
            self.death_reason = 'Food'

    def sleep_loss(self, sleep_loss):
        '''
        Принимает sleep_loss
        :param sleep_loss:то, что вычитается из pet_sleep
        :return: ничего не возвращает
        '''
        self.pet_sleep -= sleep_loss
        self.pet_hapiness_loss(0.004)
        if self.pet_sleep <= 5 or self.pet_sleep >= 106:
            self.pet_death = True
            self.death_reason = 'Sleep'

    def sleep_replenishment(self, sleep_replenishment):
        '''
        Принимает sleep_replenishment
        :param sleep_replenishment:то, что прибавляется к pet_sleep
        :return: ничего не возвращает
        '''
        self.pet_sleep += sleep_replenishment
        self.pet_hapiness_replenishment(3)
        if self.pet_sleep >= 106:
            self.pet_sleep = 106

    def set_sleep(self, pet_sleep):
        '''
        Принимает pet_sleep
        :param pet_sleep: устанавливает питомцу значение сна, которое было принято
        :return: ничего не возвращает
        '''
        self.pet_sleep = pet_sleep

    def set_hunger(self, pet_hunger):
        '''
        Принимает pet_hunger
        :param pet_hunger: устанавливает питомцу значение еды, которое было принято
        :return: ничего не возвращает
        '''
        self.pet_hunger = pet_hunger

    def set_happiness(self, pet_happiness):
        '''
        Принимает pet_happiness
        :param pet_happiness: устанавливает питомцу значение счастья, которое было принято
        :return: ничего не возвращает
        '''
        self.pet_happiness = pet_happiness

    def set_name(self, name):
        '''
        Принимает name
        :param name: устанавливает питомцу имя, которое было принято
        :return: ничего не возвращает
        '''
        self.pet_name = name

    def check_death(self):
        '''
        Ничего не принимает
        :return: возвращает death_reason, если питомец умер
        '''
        if self.pet_death == True:
            return self.death_reason
