from unittest import TestCase, main


class CustomMap:
    def __init__(self, dictionary, func_1, func_2):
        self._iter = iter(dictionary.items())
        self.func_1 = func_1
        self.func_2 = func_2

    def __call__(self):
        return list(self)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            elem = next(self._iter)
            return self.func_1(elem[0]), self.func_2(elem[1])
        except StopIteration as ex:
            raise ex

    def get_list(self):
        return list(self)


# Another way of writing an iterator

class CustomMapSecond:
    class CustomMapIterator:

        def __init__(self, collection: dict, func_1, func_2):
            self.collection = list(collection.items())
            self.func_1 = func_1
            self.func_2 = func_2
            self.pointer = 0

        def __next__(self):
            try:
                elem = self.collection[self.pointer]
                self.pointer += 1
                return self.func_1(elem[0]), self.func_2(elem[1])
            except IndexError:
                raise StopIteration

    def __init__(self, collection: dict, func_1, func_2):
        self.collection = collection
        self.func_1 = func_1
        self.func_2 = func_2

    def __iter__(self):
        return self.CustomMapIterator(self.collection, self.func_1, self.func_2)

    def get_list(self):
        return list(self)


# Tests

class TestCustomMap(TestCase):
    dict_for_test = {1: '1', 2: '2', 3: '3'}

    def setUp(self) -> None:
        self.custom_map = CustomMap(
            self.dict_for_test,
            lambda x: x ** 2,
            lambda x: x + '!'
        )

    def test_custom_map_positive_case(self):
        self.assertEqual(list(self.custom_map), [(1, '1!'), (4, '2!'), (9, '3!')])

    def test_custom_map_negative_case(self):
        self.assertNotEqual(list(self.custom_map), [(1, '1'), (4, '2'), (9, '3')])

    def test_custom_map_get_list(self):
        self.assertEqual(self.custom_map.get_list(), [(1, '1!'), (4, '2!'), (9, '3!')])


class TestCustomMapSecond(TestCase):
    dict_for_test = {1: '1', 2: '2', 3: '3'}

    def setUp(self) -> None:
        self.custom_map = CustomMapSecond(
            self.dict_for_test,
            lambda x: x ** 2,
            lambda x: x + '!'
        )

    def test_custom_map_positive_case(self):
        self.assertEqual(list(self.custom_map), [(1, '1!'), (4, '2!'), (9, '3!')])

    def test_custom_map_negative_case(self):
        self.assertNotEqual(list(self.custom_map), [(1, '1'), (4, '2'), (9, '3')])

    def test_custom_map_get_list(self):
        self.assertEqual(self.custom_map.get_list(), [(1, '1!'), (4, '2!'), (9, '3!')])


if __name__ == "main":
    main()
