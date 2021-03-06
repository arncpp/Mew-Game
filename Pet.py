from PetGlobals import Globals


class Pet:
    def __init__(self, pet_health, pet_sleep, pet_happiness, pet_hunger,
                 pet_max_stats, pet_min_stats):
        """
        Основной класс питомца
        :param pet_health: здоровье питомца
        :param pet_sleep: значение сна питомца
        :param pet_happiness: значение счастья питомца
        :param pet_hunger: значение голода питомца
        """
        self._pet_health = pet_health
        self._pet_sleep = pet_sleep
        self._pet_happiness = pet_happiness
        self._pet_hunger = pet_hunger
        self.pet_death = False
        self.death_reason = Globals.default_name_and_reason
        self._pet_name = Globals.default_name_and_reason
        self.pet_max_stats = pet_max_stats
        self.pet_min_stats = pet_min_stats
        self.pet_hap_loss = Globals.pet_hap_loss_num
        self.pet_hap_repl = Globals.pet_hap_repl_num

    def pet_hapiness_loss(self, pet_hap_loss):
        """
        Принимает pet_hap_loss
        :param pet_hap_loss: то, что вычитается из pet_happiness
        """
        self._pet_happiness -= pet_hap_loss
        if self._pet_happiness <= self.pet_min_stats:
            self.pet_death = True
            self.death_reason = Globals.pet_sad_reason

    def pet_hapiness_replenishment(self, hap_replenishment):
        """
        Принимает hap_replenishment
        :param hap_replenishment: то, что прибавляется к pet_happiness
        """
        self._pet_happiness += hap_replenishment
        if self._pet_happiness >= self.pet_max_stats:
            self._pet_happiness = self.pet_max_stats

    def hunger_loss(self, hung_loss):
        """
        Принимает hung_loss
        :param hung_loss: то, что вычитается из pet_hunger
        """
        self._pet_hunger -= hung_loss
        self.pet_hapiness_loss(self.pet_hap_loss)
        if self._pet_hunger <= self.pet_min_stats or \
                self._pet_hunger >= self.pet_max_stats:
            self.pet_death = True
            self.death_reason = Globals.pet_food_reason

    def hunger_replenishment(self, hung_replenishment):
        """
        Принимает hung_replenishment
        :param hung_replenishment: то, что прибавляется к pet_hunger
        """
        self._pet_hunger += hung_replenishment
        self.pet_hapiness_replenishment(self.pet_hap_repl)
        if self._pet_hunger >= self.pet_max_stats:
            self.pet_death = True
            self.death_reason = Globals.pet_food_reason

    def health_loss(self, heal_loss):
        """
        Принимает heal_loss
        :param heal_loss: то, что вычитается из pet_health
        """
        self._pet_health -= heal_loss
        self.pet_hapiness_loss(Globals.pet_hap_loss_in_health)
        if self._pet_health <= self.pet_min_stats:
            self.pet_death = True
            self.death_reason = Globals.pet_health_reason

    def health_replenishment(self, heal_replenishment):
        """
        Принимает heal_replenishment
        :param heal_replenishment: то, что прибавляется к pet_health
        """
        self._pet_health += heal_replenishment
        self.pet_hapiness_replenishment(Globals.pet_hap_repl_in_health)
        if self._pet_health >= self.pet_max_stats:
            self._pet_health = self.pet_max_stats
            self.pet_hapiness_replenishment(-Globals.pet_hap_repl_in_health)

    def sleep_loss(self, sl_loss):
        """
        Принимает sl_loss
        :param sl_loss: то, что вычитается из pet_sleep
        """
        self._pet_sleep -= sl_loss
        self.pet_hapiness_loss(Globals.pet_hap_loss_in_sleep)
        if self._pet_sleep <= self.pet_min_stats or \
                self._pet_sleep >= self.pet_max_stats:
            self.pet_death = True
            self.death_reason = Globals.pet_sleep_reason

    def sleep_replenishment(self, sl_replenishment):
        """
        Принимает sl_replenishment
        :param sl_replenishment: то, что прибавляется к pet_sleep
        """
        self._pet_sleep += sl_replenishment
        self.pet_hapiness_replenishment(self.pet_hap_repl)
        if self._pet_sleep >= self.pet_max_stats:
            self._pet_sleep = self.pet_max_stats
            self.pet_hapiness_replenishment(-self.pet_hap_repl)

    def set_sleep(self, pet_sleep):
        """
        Принимает pet_sleep
        :param pet_sleep: устанавливает питомцу значение сна,
        которое было принято
        """
        self._pet_sleep = pet_sleep

    def set_hunger(self, pet_hunger):
        """
        Принимает pet_hunger
        :param pet_hunger: устанавливает питомцу значение еды,
        которое было принято
        """
        self._pet_hunger = pet_hunger

    def set_happiness(self, pet_happiness):
        """
        Принимает pet_happiness
        :param pet_happiness: устанавливает питомцу значение счастья,
        которое было принято
        """
        self._pet_happiness = pet_happiness

    def set_health(self, pet_health):
        """
        Принимает pet_health
        :param pet_health: устанавливает питомцу значение здоровья,
        которое было принято
        """
        self._pet_health = pet_health

    def set_name(self, name):
        """
        Принимает name
        :param name: устанавливает питомцу имя, которое было принято
        """
        self._pet_name = name

    def check_death(self):
        """
        Ничего не принимает
        :return: возвращает death_reason, если питомец умер
        """
        if self.pet_death is True:
            return self.death_reason

    def get_pet_hunger(self):
        return self._pet_hunger

    def get_pet_sleep(self):
        return self._pet_sleep

    def get_pet_happiness(self):
        return self._pet_happiness

    def get_pet_health(self):
        return self._pet_health

    def get_pet_name(self):
        return self._pet_name
