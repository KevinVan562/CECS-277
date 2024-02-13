import check_input
import random


def read_file(file_name):
    """Reads the file and returns the list of words"""
    with open(file_name) as file:
        result_list = []
        for state in file:
            split_list = state.strip().split(',')
            result_list.append(split_list)
        return result_list


def get_random_state(states):
    """This function will return a random state from the list of states"""
    random_num = random.randint(0, 49)
    random_state = states[random_num]
    return random_state


def get_random_choices(states, correct_capital):
    """Pass in the list of states and the correct answer. Randomly assigns
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


def main():

    data_list = read_file("statecapitals.txt")
    random_state = get_random_state(data_list)
    choices = get_random_choices(data_list, random_state)
    print(data_list[0][1])
    print(random_state)
    print(choices)


main()
