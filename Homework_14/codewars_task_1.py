# https://www.codewars.com/kata/530045e3c7c0f4d3420001af

"""
DESCRIPTION:
Your task is to create a function that will take an integer and return the result of the look-and-say function
on that integer. This should be a general function that takes as input any positive integer,
and returns an integer; inputs are not limited to the sequence which starts with "1".

Conway's Look-and-say sequence goes like this:

Start with a number.
Look at the number, and group consecutive digits together.
For each digit group, say the number of digits, then the digit itself.
This can be repeated on its result to generate the sequence.

For example:

Start with 1.
There is one 1 --> 11
Start with 11. There are two 1 digits --> 21
Start with 21. There is one 2 and one 1 --> 1211
Start with 1211. There is one 1, one 2, and two 1s --> 111221
Sample inputs and outputs::

0 --> 10
2014 --> 12101114
9000 --> 1930
22322 --> 221322
222222222222 --> 122
"""


def look_say(n):
    str_n = str(n)
    counter = 0
    current_num = str_n[0]
    result_str = ''
    for num in str_n:
        if current_num == num:
            counter += 1
        else:
            result_str += str(counter) + current_num
            counter, current_num = 1, num

    result_str += str(counter) + current_num
    return int(result_str)


assert (look_say(0) == 10)
assert (look_say(1) == 11)
assert (look_say(21) == 1211)
assert (look_say(33333333333331) == 13311)
print('SUCCESS')
