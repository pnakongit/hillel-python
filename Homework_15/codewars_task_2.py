# https://www.codewars.com/kata/52597aa56021e91c93000cb0

"""  
DESCRIPTION:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""


def move_zeros(lst):
    lst_num, lst_zero = [], []
    for i in lst:
        if i == 0:
            lst_zero += [i]
        else:
            lst_num += [i]

    return lst_num + lst_zero


assert (move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
assert (move_zeros(
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0,
                                                                      0, 0, 0]
        )
assert (move_zeros([0, 0]) == [0, 0])
assert (move_zeros([0]) == [0])
assert (move_zeros([]) == [])
