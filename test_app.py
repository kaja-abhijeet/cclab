import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(12, 13), 25)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(6, 6), 12)

if __name__ == '__main__':
    unittest.main()
