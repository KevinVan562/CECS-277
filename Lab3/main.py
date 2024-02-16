# Name: Kevin Van & Isai Beltran
# Date: 02/12/2024
# Description: 10 question state capital quiz game. Depending on the user's correct
# answers, they will be given a score out of 10.

import random


def read_file(file_name):
    """Reads the file and returns the list of words"""
    with open(file_name) as file:
        result_list = []
        for row in file:
            split_list = row.strip().split(',')
            result_list.append(split_list)
        return result_list


def get_random_state(states):
    """This function will return a random state from the list of states"""
    random_number = random.randint(0, 49)
    random_state = states[random_number]
    return random_state


def get_random_choices(states, correct_capital):
    """Passes in the list of states and the correct answer. Randomly assigns
    three incorrect choices to a list and returns that list."""
    wrong_list = []
    count = 0
    while count < 3:
        random_num = random.randint(0, 49)
        if states[random_num] not in wrong_list and states[random_num] != correct_capital:
            wrong_list.append(states[random_num])
            count += 1
        elif states[random_num] == correct_capital:
            count = count
    wrong_list.append(correct_capital)
    random.shuffle(wrong_list)
    return wrong_list


def ask_question(correct_state, possible_answers):
    """Takes user's selection and checks if it is A,B,C,D if it isn't display
    an error messageand ask the question again"""
    while True:
        user_input = input("\nEnter Selection: ").upper()

        if user_input == 'A':
            return 0
        elif user_input == 'B':
            return 1
        elif user_input == 'C':
            return 2
        elif user_input == 'D':
            return 3
        else:
            # To not cause an unnecessary newline
            print("Invalid Input. Input choice A-D.", end="")
        pass


def main():

    data_list = read_file("statecapitals.txt")
    total_points = 0
    quiz_question = 1

    print("- State Capitals Quiz -")

    while quiz_question < 11:
        """This while loop will run 10 times and will ask the user a question"""
        correct_answer = get_random_state(data_list)
        choices = get_random_choices(data_list, correct_answer)

        print(f"{quiz_question}. The capital of {correct_answer[0]} is: ")
        # Indents in prints for readability in output
        print(f"     A. {choices[0][1]}", end=" ")
        print(f"  B. {choices[1][1]}", end=" ")
        print(f"  C. {choices[2][1]}", end=" ")
        print(f"  D. {choices[3][1]}", end=" ")

        user_selection = ask_question(
            correct_answer, choices)  # Gets user input

        if choices[user_selection][1] == correct_answer[1]:
            """If the user's selection is correct, add 1 to the total points"""
            print("Correct!")
            total_points += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer[1])

        quiz_question += 1  # increments the question number

    print("End of test. You got", total_points, "correct.")


main()
