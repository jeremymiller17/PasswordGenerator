import string
import secrets


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
