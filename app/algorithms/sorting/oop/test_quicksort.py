import unittest
from app.algorithms.sorting.oop.quicksort import QuickSort


class QuickSortAlgorithmTest(unittest.TestCase):
    def test_quick_sort_empty_array(self):
        """
        Test quick sort with an empty array.
        """
        quick_sort = QuickSort()
        self.assertEqual(quick_sort.sort([]), [])

    def test_quick_sort_unsorted_array(self):
        """
        Test quick sort with an unsorted array.
        """
        quick_sort = QuickSort()
        self.assertEqual(quick_sort.sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_quick_sort_reverse_sorted_array(self):
        """
        Test quick sort with a reverse-sorted array.
        """
        quick_sort = QuickSort()
        self.assertEqual(quick_sort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_quick_sort_single_element_array(self):
        """
        Test quick sort with an array containing a single element.
        """
        quick_sort = QuickSort()
        self.assertEqual(quick_sort.sort([1]), [1])


if __name__ == '__main__':
    unittest.main()
