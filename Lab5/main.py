# Name: Kevin Van & Isai Beltran
# Date: 02/26/2024
# Description: A dice game that awards the user points for pair, three-of-a-kind,
# or a series.

import check_input
import player


def take_turn(player):
    player.roll_dice()
    print(player)
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_series():
        print("You got a series of 3!")
    elif player.has_pair():
        print("You got a pair!")
    else:
        print("Aww. Too bad.")


def main():
    user = player.Player()
    print("-Yahtzee-")
    input = True
    while input:
        take_turn(user)
        print("Score = ", user.get_points())
        input = check_input.get_yes_no("Play again? (Y/N): ")
        print()
    print("Game Over.\nFinal Score = ", user.get_points())


main()
