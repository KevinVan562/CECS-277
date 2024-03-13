# Name: Kevin Van & Isai Beltran
# Date: 3/11/2024
# Description: A program that allows the user to encrypt or decrypt messages using two
# different types of encryption methods. Encrypted messages will read from the console
# and then written to a file called ‘message.txt’, and decrypted messages will be read
# from the ‘message.txt’ file then displayed to the console.

import atbash
import caesar_cipher
import check_input


def main():
    encryption_choice = check_input.get_int_range(
        "Secret Decoder Ring:\n1. Encrypt\n2. Decrypt\n", 1, 2)

    if encryption_choice == 1:
        encryption_type = check_input.get_int_range(
            "Enter encryption type:\n1. Atbash\n2. Caesar\n", 1, 2)
        message = input("Enter message to encrypt: ")

        if encryption_type == 1:
            atbash_cipher = atbash.Atbash()
            encrypted_message = atbash_cipher.encrypt_message(message)
            with open('message.txt', 'w') as file:
                file.write(encrypted_message)
            print('Encrypted message saved to "message.txt"')

        elif encryption_type == 2:
            shift = check_input.get_int_range("Enter shift value: ", 0, 25)
            caesar = caesar_cipher.CaesarCipher(shift)
            encrypted_message = caesar.encrypt_message(message)
            with open('message.txt', 'w') as file:
                file.write(encrypted_message)
            print('Encrypted message saved to "message.txt."')

    elif encryption_choice == 2:
        decryption_type = check_input.get_int_range(
            "Enter decryption type:\n1. Atbash\n2. Caesar\n", 1, 2)

        if decryption_type == 1:
            atbash_cipher = atbash.Atbash()
            with open('message.txt', 'r') as file:
                encrypted_message = file.read()
            decrypted_message = atbash_cipher.decrypt_message(
                encrypted_message)
            print('Reading from encrypted "message.txt"')
            print('Decrypted message:', decrypted_message)

        elif decryption_type == 2:
            shift = check_input.get_int_range("Enter shift value: ", 0, 25)
            caesar = caesar_cipher.CaesarCipher(shift)
            with open('message.txt', 'r') as file:
                encrypted_message = file.read()
            decrypted_message = caesar.decrypt_message(encrypted_message)
            print('Reading from encrypted "message.txt."')
            print('Decrypted message:', decrypted_message)


if __name__ == "__main__":
    main()
