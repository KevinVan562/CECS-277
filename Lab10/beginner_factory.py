import enemy_factory
import random
import beg_goblin
import beg_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
  def create_random_enemy(self):
    """Randomizes and constructs one of the easy enemies (EasyTroll, EasyGoblin)."""
    random_enemy = random.randint(1, 2)
    if random_enemy == 1:
      random_enemy = beg_goblin.BegGoblin()
    elif random_enemy == 2:
      random_enemy = beg_troll.BegTroll()
    return random_enemy
