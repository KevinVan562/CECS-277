import abc

class Character(abc.ABC):
  
  @property
  def name(self):
    """Returns the name of the character"""
    return self._name

  def __init__(self, n):
    """Initializes the character's name"""
    self._name = n


  def __str__(self):
    """Returns a string representation of the character"""
    abilities_str = "-Abilities-\n"
    abilities = self.abilities()
    for ability, level in abilities:
        if level > 0:
            abilities_str += f"{ability}: Level {level}\n"
    stats_str = "-Stats-\n"
    stats_str += f"Con: {self.constitution()}\n"
    stats_str += f"Str: {self.strength()}\n"
    stats_str += f"Wis: {self.wisdom()}\n"
    return f"\n{self.name}\n{abilities_str}\n{stats_str}"

  @abc.abstractmethod
  def abilities(self):
    """Defines the function for the abilities of the character"""
    pass
    
  @abc.abstractmethod
  def constitution(self):
    """Defines the function for the constitution of the character"""
    pass

  @abc.abstractmethod
  def strength(self):
    """Defines the function for the strength of the character"""
    pass

  @abc.abstractmethod
  def wisdom(self):
    """Defines the function for the wisdom of the character"""
    pass
