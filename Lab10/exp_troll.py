import entity
import random

class ExpTroll(entity.Entity):
  """Represents an expert troll enemy."""
  def __init__(self):
    random_hp = random.randint(15, 18)
    super().__init__("Vicious Troll", random_hp)

  def melee_attack(self, hero):
    """Displays the enemy's melee attack and the hero's hp afterwards."""
    self._melee_attack = random.randrange(8, 12)
    hero.take_damage(self._melee_attack)
    return "Vicious Troll slashes " + hero.name + " with its axe for " + str(self._melee_attack) + " damage."
