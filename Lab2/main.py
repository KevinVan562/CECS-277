# Name: Kevin Van & Isai Beltran
# Date: 02/07/2024
# Description: Create a program that plays the game ‘Hangman’. Randomly select a
# 5-letter word from the ‘dictionary.py’ file to use as the word the user needs to guess
# At the beginning, display the empty gallows and 5 blank spaces that represents
# the word they are supposed to guess. The repeatedly prommpt the user to guess
# a letter. If the letter is in the word, then display the letter in the correct
# space. If the letter is not in the word, then draw a part of the hangman.

from dictionary import words
import check_input
import random


def display_gallows(num_incorrect):
    """Function that displays the gallows based off the incorrect guesses made by user."""
    print("\n========")
    print("||/   | ")
    if num_incorrect == 1:
        print("||    o ")
        print("||")
        print("||")
        print("||")
    elif num_incorrect == 2:
        print("||    o ")
        print("||    |")
        print("||")
        print("||")
    elif num_incorrect == 3:
        print("||    o ")
        print("||    | ")
        print("||   /  ")
        print("||")
    elif num_incorrect == 4:
        print("||    o ")
        print("||    | ")
        print("||   / \\")
        print("||")
    elif num_incorrect == 5:
        print("||   \\o ")
        print("||    | ")
        print("||   / \\")
        print("||")
    elif num_incorrect == 6:
        print("||   \\o/")
        print("||    | ")
        print("||   / \\")
        print("||")
    else:
        print("||")
        print("||")
        print("||")
        print("||")

    print("")


def display_letters(letters):
    """Function to display the letters that have been guessed so far."""
    display = ""
    for letter in letters:
        print(letter, end=" ")
    return display


def get_letters_remaining(incorrect, correct):
    """Function to get the letters remaining in the alphabet"""
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guessed_letters = set(incorrect + correct)
    remaining_letters = list(alphabet - guessed_letters)
    remaining_letters.sort()
    return remaining_letters


def main():
    repeat = True
    while repeat:
        """
        This is the while loop that makes the game replayable after user
        has finished playing once. It depends on if the user inputs "Y" or "N"
        """
        word = random.choice(words)
        incorrect_guesses = []
        correct_guesses = ["_"] * len(word)
        num_correct = 0
        num_incorrect = 0

        while num_correct < len(word) and num_incorrect < 6:
            """
            While player has not guessed the word and has not made 6 incorrect guesses,
            this loop will continue to run. It creates the gallows and asks the player
            to guess a letter. If the letter is in the word, it will be added to the
            correct_guesses list. If the letter is not in the word, it will be added to
            the incorrect_guesses list.
            """
            print("\nIncorrect selections: ", end="")
            display_letters(incorrect_guesses)
            display_gallows(num_incorrect)
            display_letters(correct_guesses)
            print("\nLetters remaining: ", end="")
            display_letters(get_letters_remaining(
                incorrect_guesses, correct_guesses))
            print()
            guess = input("\nEnter a letter: ").upper()

            if not guess.isalpha() or len(guess) != 1:
                """Check to see if input is one letter and if player guessed it already"""
                print("\nThat is not a letter. ")
            else:
                if guess in correct_guesses or guess in incorrect_guesses:
                    print("\nYou have already used that letter. ")
                else:
                    if guess in word:
                        """If player guessed a correct letter"""
                        for i in range(len(word)):
                            if word[i] == guess:
                                correct_guesses[i] = guess
                                num_correct += 1
                        print("\nCorrect! ")
                    else:
                        """If player guessed an incorrect letter"""
                        incorrect_guesses.append(guess)
                        num_incorrect += 1
                        print("\nIncorrect! ")

        """Display the final state of the game."""
        display_gallows(num_incorrect)
        print(display_letters(correct_guesses))

        if num_correct == len(word):
            """Check if the player won."""
            print("\nYou win! ")
        else:
            print("\nSorry you lose! The word was: " + word)

        """Ask the player if they want to play again."""
        repeat = check_input.get_yes_no("\nPlay again (Y/N)? ")


main()
