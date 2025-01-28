class Entity:
  def __init__(self, name, max_hp):
    """Initializes the entity's name and max hp.
    Attributes:
      name (str): The name of the entity.
      max_hp (int): The maximum health points of the entity.
      hp (int): The current health points of the entity.
    """
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    """Returns the name of the entity."""
    return self._name

  @property
  def hp(self):
    """Returns the current health points of the entity."""
    return self._hp

  def take_damage(self, dmg):
    """Subtracts the damage from the entity's hp."""
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """Returns a string representation of the entity."""
    return self._name + ": " + str(self._hp) + "/" + str(self._max_hp)
