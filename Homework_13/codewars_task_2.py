# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

"""
DESCRIPTION:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
import string


def high(x):
    ascii_list = string.ascii_lowercase
    words = x.split()
    scores_list = []
    for word in x.split():
        scores = [sum([ascii_list.find(letter) + 1 for letter in word])]
        scores_list.append(scores)
    return words[scores_list.index(max(scores_list))]


assert (high('man i need a taxi up to ubud') == 'taxi')
assert (high('what time are we climbing up the volcano') == 'volcano')
assert (high('take me to semynak') == 'semynak')
assert (high('aa b') == 'aa')
assert (high('b aa') == 'b')
assert (high('bb d') == 'bb')
assert (high('d bb') == 'd')
assert (high("aaa b") == "aaa")

print("SUCCESS")
