import unittest
from main import MiniCalculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 4, "It's stupid, the function can't add")

    def test_subtract(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.subtract(2, 2), 0, "It's stupid, the function can't subtract")

    def test_multiply(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.multiply(2, 3), 6, "It's stupid, the function can't multiply")

    def text_divide(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.divide(4,2), 2, "It's stupid, the function can't divide")


if __name__ == '__main__':
    unittest.main()
