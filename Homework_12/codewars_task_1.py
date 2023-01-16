# https://www.codewars.com/kata/52fba2a9adcd10b34300094c
"""
Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of
the original are swapped.
For example, the transpose of:
| 1 2 3 |
| 4 5 6 |
is

| 1 4 |
| 2 5 |
| 3 6 |
The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that
the height and width of the matrix are both positive.
"""


def transpose(matrix):
    return [[y[i] for y in matrix] for i in range(len(matrix[0]))]


assert (transpose([[1]]) == [[1]])
assert (transpose([[1, 2, 3]]) == [[1], [2], [3]])
assert (transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
assert (transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]) == [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0],
                                                                               [0, 0, 1, 0, 0]])
print('success')
