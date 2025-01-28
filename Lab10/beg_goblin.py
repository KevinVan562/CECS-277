import entity
import random

class BegGoblin(entity.Entity):
  """Represents a beginner goblin enemy."""
  def __init__(self):
    random_hp = random.randint(7, 9)
    super().__init__("Easy Goblin", random_hp)

  def melee_attack(self, hero):
    """Displays the enemy's melee attack and the hero's hp afterwards."""
    self._melee_attack = random.randrange(4, 6)
    hero.take_damage(self._melee_attack)
    return "Easy Goblin slashes " + hero.name + " with its sword for " + str(self._melee_attack) + " damage."
