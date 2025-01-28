import decorator

class Fire(decorator.Decorator):
  def abilities(self):
    """Increments the Fire ability of the character by 1"""
    abilities = super().abilities()
    for ability in abilities:
      if ability[0] == "Fire":
          ability[1] += 1  # Increment the level of Fire
    return abilities

  def constitution(self):
    """Adds skill points to the constitution of the character for the Fire ability"""
    return super().constitution() - 3

  def strength(self):
    """Adds skill points to the strength of the character for the Fire ability"""
    return super().strength() - 1

  def wisdom(self):
    """Adds skill points to the wisdom of the character for the Fire ability"""
    return super().wisdom() + 5
