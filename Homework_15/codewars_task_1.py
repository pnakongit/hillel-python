# https://www.codewars.com/kata/526dbd6c8c0eb53254000110
"""
DESCRIPTION:
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None,
so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore

"""
import string


def alphanumeric(password):
    if not password:
        return False
    allow_symbols = string.ascii_letters + string.digits
    for elem in password:
        if elem not in allow_symbols:
            return False
    return True


assert (alphanumeric("hello world_") is False)
assert (alphanumeric("PassW0rd") is True)
assert (alphanumeric("     ") is False)


# варіант 2
def alphanumeric(password):
    return password.isalnum()


assert (alphanumeric("hello world_") is False)
assert (alphanumeric("PassW0rd") is True)
assert (alphanumeric("     ") is False)
