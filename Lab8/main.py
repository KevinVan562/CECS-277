# Name: Kevin Van & Isai Beltran
# Date: 3//18/2024
# Description: A game in which the user must escape three different doors.
# There are different doors and each door has a different method of escaping.

import check_input
import random
import basic_door
import locked_door
import deadbolt_door
import combo_door
import code_door


def open_door(door):
    """Passes in a door object that the user will try to unlock. Displays the description of the door"""
    print(door.examine_door())
    choice = check_input.get_int_range(
        door.menu_options(), 1, door.get_menu_max())
    print(door.attempt(choice))
    while not door.is_unlocked():
        print(door.clue())
        choice = check_input.get_int_range(
            door.menu_options(), 1, door.get_menu_max())
        print(door.attempt(choice))
    print(door.success())


def main():

    print("Welcome to the Escape Room. You must unlock 3 doors to escape...\n")
    doors = []
    for _ in range(3):
        doors_list = [basic_door.Basic_door(), locked_door.Locked_door(
        ), deadbolt_door.Deadbolt_door(), combo_door.Combo_door(), code_door.Code_door()]
        doors.append(random.choice(doors_list))
    for knobs in doors:
        open_door(knobs)
    print("Congratulations! You escaped... this time.")


main()
