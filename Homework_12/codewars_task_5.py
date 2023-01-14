# https://www.codewars.com/kata/55143152820d22cdf00001bb

"""
DESCRIPTION:
It's 9 time!

I want to count from 1 to n. How many times will I use a '9'?

9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc

Note: n will always be a positive integer.

Examples (input -> output)
8  -> 0
9  -> 1
10 -> 1
98 -> 18
100 -> 20
"""


def count_nines(n):
    counter = 0
    for i in range(1, n + 1):
        counter += str(i).count('9')

    return counter


assert (count_nines(1) == 0)
assert (count_nines(9) == 1)
assert (count_nines(100) == 20)
assert (count_nines(200) == 40)
assert (count_nines(201) == 40)
assert (count_nines(278) == 47)
assert (count_nines(280) == 48)
assert (count_nines(908) == 189)
assert (count_nines(909) == 191)
assert (count_nines(99999) == 50000)
assert (count_nines(565754) == 275645)
print('success')


# Перший варіант проходив тести, але валився по часу виконня, другий варіант пройшов.
def count_nines(n):
    x = ''.join(map(str, list(range(1, n + 1))))
    return x.count("9")


assert (count_nines(1) == 0)
assert (count_nines(9) == 1)
assert (count_nines(100) == 20)
assert (count_nines(200) == 40)
assert (count_nines(201) == 40)
assert (count_nines(278) == 47)
assert (count_nines(280) == 48)
assert (count_nines(908) == 189)
assert (count_nines(909) == 191)
assert (count_nines(99999) == 50000)
assert (count_nines(565754) == 275645)
print('success')
