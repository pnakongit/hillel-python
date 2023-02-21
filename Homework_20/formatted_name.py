from unittest import TestCase, main


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(TestCase):
    def test_formatted_name_none_type(self):
        with self.assertRaisesRegex(TypeError, "object of type 'NoneType' has no len()"):
            formatted_name('Pavlo', 'Nakon', None)

    def test_formatted_name_int_value(self):
        with self.assertRaises(TypeError):
            formatted_name(1, 'Nakon', 'Serg')

    def test_formatted_four_value(self):
        with self.assertRaises(TypeError):
            formatted_name('Pavlo', 'Nakon', 'Serg', 'Nik')

    def test_formatted_one_value(self):
        with self.assertRaises(TypeError):
            formatted_name('Pavlo')

    def test_formatted_two_value(self):
        self.assertEqual(formatted_name('Pavlo', 'Nakon'), 'Pavlo Nakon')

    def test_formatted_name_all_uppercase(self):
        self.assertEqual(formatted_name('PAVLO', 'NAKON', 'SERG'), 'Pavlo Serg Nakon')

    def test_formatted_name_all_lowercase(self):
        self.assertEqual(formatted_name('pavlo', 'nakon', 'serg'), 'Pavlo Serg Nakon')

    def test_formatted_name_return_type_value(self):
        self.assertIsInstance(formatted_name('Pavlo', 'Nakon', 'Serg'), str)


if __name__ == '__main__':
    main()
