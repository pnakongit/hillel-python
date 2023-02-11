# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python

"""
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9.
The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
Examples
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
"""
import re


def valid_ISBN10(isbn):
    if not re.search(r'^[0-9]{9}[X|\d]$', isbn):
        return False

    result = sum([(int(isbn[i]) if isbn[i] != 'X' else 10) * (i + 1) for i in range(len(isbn))]) % 11

    return True if result == 0 else False


valid_ISBN10('1112223339')

assert (valid_ISBN10('1112223339') is True)
assert (valid_ISBN10('048665088X') is True)
assert (valid_ISBN10('1293000000') is True)
assert (valid_ISBN10('1234554321') is True)
assert (valid_ISBN10('1234512345') is False)
assert (valid_ISBN10('1293') is False)
assert (valid_ISBN10('X12345678X') is False)
assert (valid_ISBN10('ABCDEFGHIJ') is False)
assert (valid_ISBN10('XXXXXXXXXX') is False)

print('SUCCESS')
