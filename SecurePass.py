import string
import secrets


class SecurePass:
    @staticmethod
    def create_password(length: int, symbols: bool, uppercase: bool):
        # Concatenates  into a unified string based on parameter values
        combination = string.ascii_lowercase + string.digits

        if symbols:
            combination += string.punctuation

        if uppercase:
            combination += string.ascii_uppercase

        combination_length = len(combination)

        gen_password = ""

        for _ in range(length):
            gen_password += combination[(secrets.randbelow(combination_length))]

        return gen_password


generator = SecurePass()
# Test creates a password that is 20 chars long, with symbols and upper/lowercase letters
print(generator.create_password(length=20, symbols=True, uppercase=True))
