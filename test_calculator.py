import unittest

from calculator import Calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = Calculator.calculator_operators("+", 4, 2)
        self.assertEqual(6, result)

    def test_subtract(self):
        result = Calculator.calculator_operators("-", 8, 3)
        self.assertEqual(5, result)

    def test_multiply(self):
        result = Calculator.calculator_operators("*", 3, 5)
        self.assertEqual(15, result)

    def test_divide(self):
        for number1, number2, result in [(4, 2, 2), (2, 4, 0.5), (-5, -5, 1)]:
            calculated_result = Calculator.calculator_operators("/", number1, number2)
            self.assertEqual(result, calculated_result)

    def test_divide_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.calculator_operators("/", 3, 0)

    def test_with_invalid_operation(self):
        result = Calculator.calculator_operators("m", 2, 4)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
