import door
import random


class Basic_door(door.Door):
    def __init__(self):
        """Randomizes the initial state of the door"""
        self._state = random.randint(1, 2)
        self._input = 0

    def examine_door(self):
        """Returns a string description of the door"""
        return "You encounterd a basic door, you can either push it or pull it to open."

    def menu_options(self):
        """Returns a string of the menu options that user can choose from when attempting to unlock the door"""
        return "1. Push\n2. Pull\n"

    def get_menu_max(self):
        """Returns the number of options in the above menu"""
        return 2

    def attempt(self, option):
        """Passes in the user’s selection"""
        self._input = option
        if option == 1:
            return "You push the door.\n"
        elif option == 2:
            return "You pull the door.\n"

    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise"""
        return self._state == self._input

    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt"""
        return "Try the other way.\n"

    def success(self):
        """Returns the congratulatory message if the user was successful"""
        return "Congratulations, you opened the door.\n"
