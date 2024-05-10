from app.algorithms.sorting.functions.quicksort import quicksort
import unittest


class TestQuicksort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(quicksort([]), [])

    def test_sorted_array(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
