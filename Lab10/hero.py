import entity
import random


class Hero(entity.Entity):
  def __init__(self, name):
    """Displays the hero's name and hp."""
    super().__init__(name, 25)
    
  def melee_attack(self, enemy):
      """Displays the hero's melee attack and the enemy's hp afterwards."""
      sword_damage = random.randrange(1, 6) + random.randrange(1, 6)
      enemy.take_damage(sword_damage)
      return "\n" + self.name + " slashes a " + enemy.name + " with a sword for " + str(sword_damage) + " damage."

  def ranged_attack(self, enemy):
      """Displays the hero's ranged attack and the enemy's hp afterwards."""
      arrow_damage = random.randrange(1, 12)
      enemy.take_damage(arrow_damage)
      return "\n" + self.name + " pierces " + enemy.name + " with an arrow for " + str(arrow_damage) + " damage."
