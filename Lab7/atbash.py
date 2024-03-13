import cipher


class Atbash(cipher.Cipher):
    def __init__(self):
        """Initializes the alphabet attribute."""
        super().__init__()

    def _encrypt_letter(self, letter):
        """Encrypts a single letter by using the reverse alphabet"""
        alphabet_index = self._alphabet_list.index(letter)
        encrypted_index = 25 - alphabet_index
        return self._alphabet_list[encrypted_index]

    def _decrypt_letter(self, letter):
        """Decrypts a single letter by using the alphabet"""
        encrypted_index = 25 - self._alphabet_list.index(letter)
        decrypted_index = encrypted_index
        return self._alphabet_list[decrypted_index]
