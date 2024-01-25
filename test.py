import unittest
from main import add_numbers


class TestAddNumbersFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7, "Ошибка: Сумма положительных чисел.")

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -5)
        self.assertEqual(result, -7, "Ошибка: Сумма отрицательных чисел.")

    def test_add_mixed_numbers(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7, "Ошибка: Сумма смешанных положительных и отрицательных чисел.")


if __name__ == '__main__':
    unittest.main()
