# Name: Kevin Van & Isai Beltran
# Date: 4/16/2024
# Description: This is a game where the Hero will try to fight a variety of monsters with different difficulties.
# Once all of the enemies are defeated, the game is won. However, if the Hero dies, then its game over.

import random
import check_input
from expert_factory import ExpertFactory
from beginner_factory import BeginnerFactory
from hero import Hero

def main():
  """Displays Hero's name and explains what the hero has to do"""
  print("Monster Trials")
  username = input("What is your name? ")
  h = Hero(username)
  valid = True
  print("\nYou will face a series of 3 monsters, " + username + ".\nDefeat them all to win.")

  monsters = []
  monsters.extend(BeginnerFactory().create_random_enemy() for _ in range(2))
  monsters.append(ExpertFactory().create_random_enemy())

  while valid:
      """Displays the options the hero can choose"""
      print("\nChoose an enemy to attack: ")
      for i, monster in enumerate(monsters): # prints the monsters in the list
          print(f"{i+1}. {monster}")
      choice = check_input.get_int_range("Enter choice: ", 1, len(monsters))
      selected_monster = monsters[choice - 1]
      print()
      print(h)
      print("1. Sword Attack\n2. Arrow Attack")
      attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)

      if attack_choice == 1:
          print(h.melee_attack(selected_monster))
      elif attack_choice == 2:
          print(h.ranged_attack(selected_monster))

      attacking_monster = random.choice(monsters)
      if attacking_monster.hp > 0:
          print(attacking_monster.melee_attack(h))

      if h.hp <= 0:
        """If the hero's hp is 0 or less, the game ends"""
        print("\nGame Over! You have been defeated.")
        valid = False
        break

      if selected_monster.hp <= 0:
        """If the monster's hp is 0 or less, the monster is removed from the list"""
        print(f"You have slain the {selected_monster.name}")
        monsters.remove(selected_monster)

      if not monsters:
        """If the list is empty, the game ends"""
        print("\nCongratulations! You defeated all three monsters!\nGame Over")
        valid = False
        break

if __name__ == "__main__":
    main()
