import unittest
from main import MiniCalculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 4, "It's stupid, the function can't add")


if __name__ == '__main__':
    unittest.main()