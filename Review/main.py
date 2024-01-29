import check_input


def main():
    val = check_input.get_int_range("Enter a number 1-10: ", 1, 10)

    print("Val = " + str(val))


main()
