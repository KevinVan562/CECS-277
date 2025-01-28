# Name: Kevin Van & Isai Beltran
# Date: 4/24/2024
# Description: A game where the player has the choice to create a character of his/her own.
# The player can name the created character.
# The character is then given a set of abilities that the player can choose from.
# The player can then choose to add the abilities to their character.


import archery
import fire
import fighting
import healing
import dwarf
import elf
import halfling
import check_input

def main():
  print("Character Maker!")
  print("Choose your character:")
  print("1. Dwarf\n2. Elf\n3. Halfling")

  character_selection = check_input.get_int_range("Enter Choice: ", 1, 3)
  character_name = input("\nWhat is your character's name? ")

  if character_selection == 1:
      character = dwarf.Dwarf(character_name)
  elif character_selection == 2:
      character = elf.Elf(character_name)
  elif character_selection == 3:
      character = halfling.Halfling(character_name)
  else:
      print("Invalid choice")
      return

  points_available = 5

  while points_available > 0:
      print(str(character))
      print("You have " + str(points_available) + " points left to spend.")
      print("Add an ability:")
      print("1. Archery\n2. Fighting\n3. Fire\n4. Healing")
      ability_selection = check_input.get_int_range("Enter Choice: ", 1, 4)
      if ability_selection == 1:
          character = archery.Archery(character)
      elif ability_selection == 2:
          character = fighting.Fighting(character)
      elif ability_selection == 3:
          character = fire.Fire(character)
      elif ability_selection == 4:
          character = healing.Healing(character)
      else:
          print("Invalid choice")
      points_available -= 1

  if points_available <= 0:
      print("Congratulations! You have created your character")

if __name__ == "__main__":
  main()


