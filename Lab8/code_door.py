import random
import door


class Code_door(door.Door):

    def __init__(self):
        """Randomizes the initial state of the door"""
        self._correct_code = [random.choice(["X", "O"]) for x in range(3)]
        self._input = [random.choice(["X", "O"]) for x in range(3)]

    def examine_door(self):
        """Returns a string description of the door"""
        return "A door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’.\n"

    def menu_options(self):
        """Returns a string of the menu options that user can choose from when attempting to unlock the door"""
        return "1. Press key 1 \n2. Press key 2 \n3. Press key 3\n"

    def get_menu_max(self):
        """Returns the number of options in the above menu"""
        return 3

    def attempt(self, option):
        """Passes in the user’s selection. Uses that value to update the attributes that are needed to determine whether the user has unlocked the door"""
        if self._input[option-1] == "X":
            self._input[option-1] = "O"
        elif self._input[option-1] == "O":
            self._input[option-1] = "X"
        return f"You press key {option}. The keypad states: {''.join(self._input)}"

    def is_unlocked(self):
        """Checks to see if the door was unlocked, returns true if it is, false otherwise"""
        return self._correct_code == self._input

    def clue(self):
        """Returns the hint that is returned if the user was unsuccessful at their attempt"""
        correct = 0
        for c in range(len(self._correct_code)):
            if self._correct_code[c] == self._input[c]:
                correct += 1
        return f"{correct} of the correct characters are in the correct position.\n"

    def success(self):
        """Returns the congratulatory message if the user was successful"""
        return "Congratulations, you cracked the code and opened the door.\n"
