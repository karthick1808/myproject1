import unittest

class TestModule2(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_division(self):
        self.assertEqual(8 / 2, 4)

if __name__ == '__main__':
    unittest.main()
