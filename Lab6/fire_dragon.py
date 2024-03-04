import random
import dragon


class FireDragon(dragon.Dragon):

    def __init__(self, name, max_hp, f_shots):
        super().__init__(name, max_hp)
        self._fire_shots = f_shots

    def special_attack(self, hero):
        if self._fire_shots > 0:
            fire_attack = random.randrange(5, 9)
            self._fire_shots -= 1
            hero.take_damage(fire_attack)
            return "\n" + self._name + " shot fire attack! " + " for " + str(fire_attack) + " damage!"
        else:
            return "\n" + self._name + " failed a fire attack"

    def __str__(self):
        return super().__str__() + " \n Fire Shots Remaining: " + str(self._fire_shots)
