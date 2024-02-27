# Name: Kevin Van & Isai Beltran
# Date: 02/19/2024
# Description: Create a program that allows the user to view, search, and modify a contact
# list made up of contact objects. A contact has a name, phone number, address, city,
# and zip code. Contacts are initially read in from the file ‘addresses.txt’ and then
# are written back to the file when the program ends.

import check_input
import contact


def read_file():
    """Reads the file and returns a list of sorted contacts"""
    contacts = []
    with open("addresses.txt", "r") as file:
        for line in file:
            fn, ln, pn, addr, city, zip_code = line.strip().split(",")
            new_contact = contact.Contact(fn, ln, pn, addr, city, zip_code)
            contacts.append(new_contact)
    contacts.sort()
    return contacts


def write_file(contacts):
    """Writes the list of contacts to the file"""
    with open("addresses.txt", "w") as file:
        for c in contacts:
            file.write(repr(c))


def get_menu_choice():
    """Displays the Rolodex menu and returns the user's choice"""
    print("Rolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Save and Quit")
    choice = check_input.get_int_range("", 1, 5)
    return choice


def modify_contact(con):
    """Modifies a contact in the list"""
    while True:
        print("Modify Menu: ")
        print("1. First name ")
        print("2. Last name ")
        print("3. Phone ")
        print("4. Address ")
        print("5. City ")
        print("6. Zip ")
        print("7. Save ")
        choice = check_input.get_int_range("", 1, 7)

        if choice == 1:
            new_fn = input("Enter new first name: ")
            con.fn = new_fn
        elif choice == 2:
            new_ln = input("Enter new last name: ")
            con.ln = new_ln
        elif choice == 3:
            new_pn = input("Enter new phone #: ")
            con.pn = new_pn
        elif choice == 4:
            new_addr = input("Enter new address: ")
            con.addr = new_addr
        elif choice == 5:
            new_city = input("Enter new city: ")
            con.city = new_city
        elif choice == 6:
            new_zip = input("Enter new zip code: ")
            con.zip_code = new_zip
        elif choice == 7:
            print("Contact saved.")
            break


def main():
    contacts = read_file()
    while True:
        """While loop that displays the menu and calls the appropriate function"""
        choice = get_menu_choice()
        print()
        if choice == 1:
            """Displays the contacts"""
            for i, cont in enumerate(contacts, 1):
                print(f"{i}. {str(cont)}")
        elif choice == 2:
            """Adds a contact to the list"""
            print("Enter new contact: ")
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            pn = input("Enter phone #: ")
            addr = input("Enter address: ")
            city = input("Enter city: ")
            zip_code = input("Enter zip code: ")
            new_contact = contact.Contact(fn, ln, pn, addr, city, zip_code)
            contacts.append(new_contact)
            contacts = sorted(contacts)
            print()
        elif choice == 3:
            """Searches for a contact in the list"""
            choice = check_input.get_int_range(
                "1. Search by last name \n2. Search by zip\n", 1, 2)
            if choice == 1:
                """Search by last name"""
                last_name = input("Enter last name: ")
                found = False
                for con in contacts:
                    if con.ln == last_name:
                        print(con)
                        found = True
                        break
            elif choice == 2:
                """Search by zip"""
                zip_code = input("Enter zip code: ")
                found = False
                for con in contacts:
                    if con.zip_code == zip_code:
                        print(con)
                        found = True
        elif choice == 4:
            """Modify contact"""
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            found = False
            for con in contacts:
                if con.fn == first_name and con.ln == last_name:
                    print(f"{con}\n")
                    modify_contact(con)
                    write_file(contacts)
                    found = True
            if not found:
                print("Contact not found.")
            contacts = sorted(contacts)
        elif choice == 5:
            """Saves and quits"""
            write_file(contacts)
            print("Saving File...")
            print("Ending Program")
            break


if __name__ == "__main__":
    main()
