import enemy_factory
import random
import exp_goblin
import exp_troll

class ExpertFactory(enemy_factory.EnemyFactory):
  def create_random_enemy(self):
    """Randomizes and constructs one of the easy enemies (ExpertTroll, ExpertGoblin)."""
    random_enemy = random.randint(1, 2)
    if random_enemy == 1:
      random_enemy = exp_goblin.ExpGoblin()
    elif random_enemy == 2:
      random_enemy = exp_troll.ExpTroll()
    return random_enemy
