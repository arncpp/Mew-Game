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

    def hunger_loss(self, hunger_loss):
        self.pet_hunger -= hunger_loss
        if self.pet_hunger <= 5 or self.pet_hunger >= 105:
            self.pet_death = True
            self.death_reason = 'Food'

    def hunger_replenishment(self, hunger_replenishment):
        self.pet_hunger += hunger_replenishment
        if self.pet_hunger >= 105:
            self.pet_death = True
            self.death_reason = 'Food'

    def sleep_loss(self, sleep_loss):
        self.pet_sleep -= sleep_loss
        if self.pet_sleep <= 5 or self.pet_sleep >= 105:
            self.pet_death = True
            self.death_reason = 'Sleep'

    def set_sleep(self, pet_sleep):
        self.pet_sleep = pet_sleep

    def sleep_replenishment(self, sleep_replenishment):
        self.pet_sleep += sleep_replenishment
        if self.pet_sleep >= 105:
            self.pet_death = True
            self.death_reason = 'Sleep'

    def set_hunger(self, pet_hunger):
        self.pet_hunger = pet_hunger

    def check_death(self):
        if self.pet_death == True:
            return self.death_reason

    def set_name(self, name):
        self.pet_name = name
