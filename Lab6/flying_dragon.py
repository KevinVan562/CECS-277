import random
import dragon


class FlyingDragon(dragon.Dragon):

    def __init__(self, name, max_hp, swoops):
        super().__init__(name, max_hp)
        self._swoops = swoops

    def special_attack(self, hero):
        if self._swoops > 0:
            swoops_attack = random.randrange(5, 8)
            self._swoops -= 1
            hero.take_damage(swoops_attack)
            return "\n" + self._name + " attacked with swoos attack! " + " for " + str(swoops_attack) + " damage!"
        else:
            return "\n" + self._name + " failed a swoops attack"

    def __str__(self):
        return super().__str__() + " \n Swoops Remaining: " + str(self._swoops)
