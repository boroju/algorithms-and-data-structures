import unittest
from app.algorithms.sorting.oop.mergesort import MergeSort


class MergeSortAlgorithmTest(unittest.TestCase):
    def test_merge_sort_empty_array(self):
        """
        Test merge sort with an empty array.
        """
        merge_sort = MergeSort()
        self.assertEqual(merge_sort.sort([]), [])

    def test_merge_sort_unsorted_array(self):
        """
        Test merge sort with an unsorted array.
        """
        merge_sort = MergeSort()
        self.assertEqual(merge_sort.sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_merge_sort_reverse_sorted_array(self):
        """
        Test merge sort with a reverse-sorted array.
        """
        merge_sort = MergeSort()
        self.assertEqual(merge_sort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_merge_sort_single_element_array(self):
        """
        Test merge sort with an array containing a single element.
        """
        merge_sort = MergeSort()
        self.assertEqual(merge_sort.sort([1]), [1])


if __name__ == '__main__':
    unittest.main()
