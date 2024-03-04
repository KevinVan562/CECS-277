import random
import entity


class Dragon(entity.Entity):

    def basic_attack(self, hero):
        tail_attack = random.randrange(1, 6)
        hero.take_damage(tail_attack)
        return "\n" + self.name + "smashes you with its tail " + "for" + str(tail_attack) + " damage"

    def special_attack(self, hero):
        claw_attack = random.randrange(1, 12)
        hero.take_damage(claw_attack)
        return "\n" + self.name + "slashes you with its claw " + "for" + str(claw_attack) + " damage"
