import entity
import random


class Hero(entity.Entity):

    def sword_attack(self, dragon):
        sword_damage = random.randrange(1, 6) + random.randrange(1, 6)
        dragon.take_damage(sword_damage)
        return "\n" + self.name + " slashed " + dragon.name + " for " + str(sword_damage) + " damage"

    def arrow_attack(self, dragon):
        arrow_damage = random.randrange(1, 12)
        dragon.take_damage(arrow_damage)
        return "\n" + self.name + " hit " + dragon.name + " for " + str(arrow_damage) + " damage"
