from typing import List
from app.algorithms.sorting.oop.sort_algorithms import SortAlgorithm


class QuickSort(SortAlgorithm):
    def sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array in non-decreasing order using the quicksort algorithm.

        Args:
            arr (List[int]): The input array to be sorted.

        Returns:
            List[int]: The sorted array.
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.sort(left) + middle + self.sort(right)
