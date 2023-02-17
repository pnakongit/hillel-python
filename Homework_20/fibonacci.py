from unittest import TestCase, main


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]
a = Fibonacci()
print(a(0))

class TestFibonacci(TestCase):
    fibonacci = Fibonacci()

    def tearDown(self) -> None:
        self.fibonacci.cache = [0, 1]

    def test_fibonacci_zero(self):
        self.assertEqual(self.fibonacci(0),0)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_fibonacci_not_int(self):
        values = [(10,), '10', [10, ], {10, }]
        for value in values:
            with self.assertRaises(ValueError, msg=f'Value type : {type(value)}'):
                self.fibonacci(value)

    def test_fibonacci_error_msg(self):
        value = -5
        with self.assertRaisesRegex(ValueError, f'Positive integer number expected, got "{value}"'):
            self.fibonacci(value)

    def test_fibonacci_positive_case_ten(self):
        self.assertEqual(self.fibonacci(10), 55)

    def test_fibonacci_positive_big_value(self):
        self.assertEqual(
            self.fibonacci(400), 176023680645013966468226945392411250770384383304492191886725992896575345044216019675
        )

    def test_fibonacci_negative_case_nine(self):
        self.assertNotEqual(self.fibonacci(9), 55)

    def test_fibonacci_return_type_value(self):
        self.assertIsInstance(self.fibonacci(5), int)


if __name__ == '__main__':
    main()
