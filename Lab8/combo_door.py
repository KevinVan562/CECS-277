import door
import random


class Combo_door(door.Door):
    def __init__(self):
        """Randomizes the initial state of the door (a number between 1-10) and the correct value"""
        self._correct_value = random.randint(1, 10)
        self._input = 0

    def examine_door(self):
        """Returns a string description of the door"""
        return "You encounterd a combination door, you need to enter the correct combination to unlock the door.\n"

    def menu_options(self):
        """Returns a string of the menu options that user can choose from when attempting to unlock the door"""
        return "Enter a number 1-10:\n"

    def get_menu_max(self):
        """Returns the number of options in the above menu"""
        return 10

    def attempt(self, option):
        """Passes in the user’s selection"""
        self._input = option
        return f"You turn the dial to ... {option}\n"

    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise"""
        return self._correct_value == self._input

    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt"""
        if self._correct_value > self._input:
            return "Try a higher number.\n"
        else:
            return "Try a lower number.\n"

    def success(self):
        """Returns the congratulatory message if the user was successful"""
        return "You found the correct combination and opened the door.\n"
