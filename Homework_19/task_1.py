# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

"""
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the
weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list".
It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can you give this string ordered by
"weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering)
and not numbers:

180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between
two consecutive numbers
For C: The result is freed.

"""


# bubble sort
def order_weight(strng):
    if not strng:
        return ""

    list_strng = strng.split()
    for i in range(len(list_strng)):
        for j in range(i + 1, len(list_strng)):
            if sum(map(int, list(list_strng[i]))) > sum(map(int, list(list_strng[j]))):
                list_strng[i], list_strng[j] = list_strng[j], list_strng[i]
            if sum(map(int, list(list_strng[i]))) == sum(map(int, list(list_strng[j]))):
                if list_strng[i] > list_strng[j]:
                    list_strng[i], list_strng[j] = list_strng[j], list_strng[i]

    return ' '.join(list_strng)


assert (order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99")
assert (order_weight(
    "2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999")
assert (order_weight("") == "")

print('SUCCESS')


# function sorted
def order_weight(strng):
    list_strng = strng.split()
    return ' '.join(sorted(list_strng, key=lambda x: (sum(map(int, x)), x)))


assert (order_weight("103 123 4444 99 2000") == "2000 103 123 4444 99")
assert (order_weight(
    "2000 10003 1234000 44444444 9999 11 11 22 123") == "11 11 2000 10003 22 123 1234000 44444444 9999")
assert (order_weight("") == "")

print('SUCCESS')
