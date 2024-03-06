# Name: Kevin Van & Isai Beltran
# Date: 3/4/2024
# Description: Create a game where the user must defeat three dragons to pass the trails.
# Use inheritance to implement the following class diagram in your program.

import random
import hero
import dragon
import fire_dragon
import flying_dragon
import check_input


def main():
    """Displays the name of the hero and the dragons, and prompts the user to choose a dragon to attack."""
    username = input("What is your name, challenger? ")
    player = hero.Hero(username, 50)
    print("Welcome to dragon training, " +
          username + ".\nYou must defeat 3 dragons.")
    dragons = [dragon.Dragon("Deadly Nadder", 10), fire_dragon.FireDragon(
        "Gronckle", 15, 3), flying_dragon.FlyingDragon("Timberjack", 20, 5)]

    while len(dragons) > 0:  # Displays the amount of dragons still alive.
        print("\n" + username + ": " + str(player.hp) + "/50")
        for i in range(len(dragons)):
            print(f"{i + 1}. Attack {dragons[i]}")

        # User gets to choose a dragon to attack.
        dragon_choice = check_input.get_int_range(
            "Choose a dragon to attack: ", 1, len(dragons)) - 1
        print("\nAttack with: \n1. Arrow (1 D12) \n2. Sword (2 D6)")

        # User gets to choose an attack. Sword or arrow.
        attack_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
        if attack_choice == 1:
            print(player.arrow_attack(dragons[dragon_choice]))
        elif attack_choice == 2:
            print(player.sword_attack(dragons[dragon_choice]))

        if dragons[dragon_choice].hp <= 0:
            # Removes the dragon from the list if it has 0 hp.
            dragons.pop(dragon_choice)
            if len(dragons) == 0:
                # Once all dragons are defeated, user wins.
                print(
                    "\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
            continue

        # Randomly chooses a dragon to attack the player.
        dragon_choice = random.randint(0, len(dragons) - 1)
        # Randomly chooses dragon's attack.
        attack_choice = random.randint(1, 2)

        if attack_choice == 1:  # Shows the different attacks the dragon can do.
            print(dragons[dragon_choice].basic_attack(player))
        elif attack_choice == 2:
            print(dragons[dragon_choice].special_attack(player))

        if player.hp <= 0:  # If the player has 0 hp, the game ends.
            print("You have been defeated.")
            break


if __name__ == "__main__":
    main()
