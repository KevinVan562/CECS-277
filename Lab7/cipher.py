import abc


class Cipher(abc.ABC):

    def __init__(self):
        """Initializes the alphabet attribute."""
        self._alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Getter for the alphabet
    @property
    def alphabet(self):
        return self._alphabet_list

    @abc.abstractmethod
    def _encrypt_letter(self, letter):
        pass

    @abc.abstractmethod
    def _decrypt_letter(self, letter):
        pass

    def encrypt_message(self, message):
        """Encrypts a message."""
        message = message.upper()
        encrypted_characters = []
        for char in message:
            if char in self._alphabet_list:
                encrypted_characters.append(self._encrypt_letter(char))
            else:
                encrypted_characters.append(char)
        return ''.join(encrypted_characters)

    def decrypt_message(self, message):
        """Decrypts an encrypted message."""
        message = message.upper()
        decrypted_characters = []
        for char in message:
            if char in self._alphabet_list:
                decrypted_characters.append(self._decrypt_letter(char))
            else:
                decrypted_characters.append(char)
        return ''.join(decrypted_characters)
