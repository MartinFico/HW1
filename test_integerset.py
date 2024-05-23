import unittest
from integerset import IntegerSet

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.int_set = IntegerSet()

    def test_add_and_sum(self):
        self.int_set.add(1)
        self.int_set.add(2)
        self.int_set.add(3)
        self.assertEqual(self.int_set.sum(), 6)

    def test_mean(self):
        self.int_set.add(1)
        self.int_set.add(2)
        self.int_set.add(3)
        self.assertEqual(self.int_set.mean(), 2)

    def test_max(self):
        self.int_set.add(1)
        self.int_set.add(2)
        self.int_set.add(3)
        self.assertEqual(self.int_set.max(), 3)

    def test_min(self):
        self.int_set.add(1)
        self.int_set.add(2)
        self.int_set.add(3)
        self.assertEqual(self.int_set.min(), 1)

    def test_empty_set(self):
        self.assertEqual(self.int_set.sum(), 0)
        self.assertEqual(self.int_set.mean(), 0)
        self.assertIsNone(self.int_set.max())
        self.assertIsNone(self.int_set.min())

    def test_duplicates(self):
        self.int_set.add(1)
        self.int_set.add(1)
        self.assertEqual(self.int_set.sum(), 1)
        self.assertEqual(self.int_set.mean(), 1)
        self.assertEqual(self.int_set.max(), 1)
        self.assertEqual(self.int_set.min(), 1)

    def test_initial_elements(self):
        initial_set = IntegerSet([4, 5, 6])
        self.assertEqual(initial_set.sum(), 15)
        self.assertEqual(initial_set.mean(), 5)
        self.assertEqual(initial_set.max(), 6)
        self.assertEqual(initial_set.min(), 4)

if __name__ == '__main__':
    unittest.main()