import abc

class EnemyFactory(abc.ABC):
  """Creates a random enemy."""
  @abc.abstractmethod
  def create_random_enemy(self):
    pass
