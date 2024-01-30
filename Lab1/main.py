# Name: Kevin Van &
# Date: 01/29/2024
# Description: Create a program that allows the user to play the Shell Game, where a player
# bets that they can guess the location of the ball under a set of three shells or cups.
# The user should start the game with $100. Hide the ball in one of three places by randomizing
# its location with a value between 1 and 3. Prompt the user to enter an amount to bet.
# Then prompt the user to enter their guess for where the ball is hidden. If it is a match
# then the user receives double their bet. Display the location of the ball and tell the user
# if they were correct or not. Repeat the game until the user runs out of money or decides to quit.

import random
import check_input


def main():
    print("Find the ball to double your bet!")
    print("You have $100")
    money = 100

    while money > 0:
        bet_amount = check_input.get_int_range("Bet amount? ", 1, money)
        cups = 1, 2, 3
        ball = random.choice(cups)
        print("  _____       _____       _____")
        print(" /     \\    /     \\    /     \\")
        print("/   1   \\  /   2   \\  /   3   \\")
        print("----------  ----------  ----------")
        guess = check_input.get_int_range("Make a guess:  ", 1, 3)
        """Check to see if guess is correct or not"""
        if guess == ball:
            print("Congratulations!")
            money += bet_amount * 2
            print("You have $" + str(money))
        elif guess != ball:
            print("Sorry... you lose.")
            print("The ball is under cup", ball)
            money -= bet_amount
            print("You have $" + str(money))

        """If player runs out of money, Game Over!"""
        if money == 0:
            print("You're out of money. Game over.")
            return 0

        """Ask player if they want to play again if balance is greater than 0"""
        repeat = check_input.get_yes_no("Play again? (Y/N) ")
        """If player chooses yes, the game will continue & If no it will end"""
        if repeat is True:
            bet_amount = check_input.get_int_range("Bet amount? ", 1, money)
            cups = 1, 2, 3
            ball = random.choice(cups)
            guess = check_input.get_int_range("Make a guess: ", 1, 3)

            if guess == ball:
                print("Congratulations!")
                money += bet_amount * 2
                print("You have $" + str(money))
            else:
                print("You lost!")
                print("The ball is under cup", ball)
                money -= bet_amount
                print("You have $" + str(money))
        elif repeat is False:
            return 0


main()
