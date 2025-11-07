import unittest
from app.algorithms.sorting.functions.mergesort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
