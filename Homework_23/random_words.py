from english_words import get_english_words_set
from random import choice
from unittest import TestCase, main


def random_words(max_words):
    if max_words > 10_000 or max_words <= 0 or not isinstance(max_words, int):
        raise ValueError(f'Must be positive integer numbers, got {max_words}')

    words = list(get_english_words_set(['web2']))

    words_unique = set()
    while len(words_unique) < max_words:
        words_unique.add(choice(words))

    for i in words_unique:
        yield i


# Tests

class TestRandomWords(TestCase):

    def test_random_words_unique(self):
        self.assertEqual(len(set(random_words(100))), 100)

    def test_random_words_min(self):
        self.assertEqual(len(list(random_words(1))), 1)

    def test_random_words_max(self):
        self.assertEqual(len(list(random_words(10_000))), 10_000)

    def test_random_words_zero(self):
        with self.assertRaises(ValueError):
            next(random_words(0))

    def test_random_words_max_plus_one(self):
        with self.assertRaises(ValueError):
            next(random_words(10_001))

    def test_random_words_negative_value(self):
        with self.assertRaises(ValueError):
            next(random_words(-10))

    def test_random_words_str(self):
        result = all([i.isalpha() for i in random_words(10_000)])
        self.assertTrue(result)


if __name__ == 'main':
    main()
