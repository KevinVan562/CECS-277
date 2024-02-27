"""

Name: Kevin Van & Isai Beltran
Date: 01/29/2024
Description: Create a program that allows the user to play the Shell Game
where a player bets that they can guess the location of the ball under a set
of three shellsor cups.The user should start the game with $100. Hide the ball
in one of three places by randomizing its location with a value between
1 and 3. Prompt the user to enter an amount to bet.Then prompt the user
to enter their guess for where the ball is hidden. If it is a match then
the user receives double their bet. Display the location of the ball and
tell the user if they were correct or not. Repeat the game until the user
runs out of money or decides to quit.

"""

import random
import check_input


def main():

    print("Find the ball to double your bet!")
    print("You have $100")
    currentBalance = 100
    canPlay = currentBalance > 0

    while canPlay:
        bet = check_input.get_int_range("Bet amount? ", 1, currentBalance)
        currentBalance -= bet
        cups = (1, 2, 3)
        ball = random.choice(cups)
        print("  _____      _____       _____")
        print(" /     \\    /     \\     /     \\")
        print("/   1   \\  /   2   \\   /   3   \\")
        print("---------- ----------  ----------")
        guess = check_input.get_int_range("Make a guess: ", 1, 3)

        if guess == 1 and ball == 1:
            print("  _____      _____       _____")
            print(" /     \\    /     \\     /     \\")
            print("/   o   \\  /       \\   /       \\")
            print("---------- ----------  ----------")
            print("Congratulations!")
            currentBalance += bet * 2
            print("You have $" + str(currentBalance))

        elif guess == 2 and ball == 2:
            print("  _____      _____       _____")
            print(" /     \\    /     \\     /     \\")
            print("/       \\  /   o   \\   /       \\")
            print("---------- ----------  ----------")
            print("Congratulations!")
            currentBalance += bet * 2
            print("You have $" + str(currentBalance))

        elif guess == 3 and ball == 3:
            print("  _____      _____       _____")
            print(" /     \\    /     \\     /     \\")
            print("/       \\  /       \\   /   o   \\")
            print("---------- ----------  ----------")
            print("Congratulations!")
            currentBalance += bet * 2
            print("You have $" + str(currentBalance))

        elif guess != ball:
            print("Sorry... you lose.")
            print("The ball is under cup", ball)
            currentBalance -= bet
            print("You have $" + str(currentBalance))

        canPlay = currentBalance > 0 and check_input.get_yes_no("Play again? (Y/N)")

    if currentBalance <= 0:
        print("You're out of money! Game over.")


main()
