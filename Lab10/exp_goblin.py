import entity
import random

class ExpGoblin(entity.Entity):
  """Represents an expert goblin enemy."""
  def __init__(self):
    random_hp = random.randint(12, 15)
    super().__init__("Vicious Goblin", random_hp)

  def melee_attack(self, hero):
    """Displays the enemy's melee attack and the hero's hp afterwards."""
    self._melee_attack = random.randrange(5, 8)
    hero.take_damage(self._melee_attack)
    return "Vicious Goblin slashes " + hero.name + " with its sword for " + str(self._melee_attack) + " damage."
