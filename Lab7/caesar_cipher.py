import cipher


class CaesarCipher(cipher.Cipher):
    def __init__(self, shift):
        """Initializes the alphabet attribute and the shift value."""
        super().__init__()
        self._shift = shift % 26
        if not (0 <= shift < 26):
            raise ValueError("Shift value must be between 0 and 25.")

    def _encrypt_letter(self, letter):
        """Encrypts a single letter by shifting it by the shift value."""
        return self._alphabet_list[(self._alphabet_list.index(letter) + self._shift) % 26]

    def _decrypt_letter(self, letter):
        """Decrypts a single letter by shifting it by the negative of the shift value."""
        return self._alphabet_list[(self._alphabet_list.index(letter) - self._shift) % 26]
