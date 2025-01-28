import character

class Dwarf(character.Character):
    def __init__(self, n):
      """Initializes the Dwarf character with a name"""
      super().__init__(n + " the Dwarf")

    def abilities(self):
      """Returns a list of the abilities of the character"""
      return [["Archery", 0], ["Fighting", 1], ["Fire", 0], ["Healing", 0]]

    def constitution(self):
      """Returns the constitution level of the character"""
      return 13

    def strength(self):
      """Returns the strength level of the character"""
      return 15

    def wisdom(self):
      """Returns the wisdom level of the character"""
      return 10

