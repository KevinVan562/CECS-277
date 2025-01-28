import entity
import random

class BegTroll(entity.Entity):
  """Represents a beginner troll enemy."""
  def __init__(self):
    random_hp = random.randint(8, 10)
    super().__init__("Easy Troll", random_hp)

  def melee_attack(self, hero):
    """Displays the enemy's melee attack and the hero's hp afterwards."""
    self._melee_attack = random.randrange(5, 9)
    hero.take_damage(self._melee_attack)
    return "Easy Troll slashes " + hero.name + " with its axe for " + str(self._melee_attack) + " damage."
