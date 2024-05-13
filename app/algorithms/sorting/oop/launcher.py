from app.algorithms.sorting.oop.mergesort import MergeSort
from app.algorithms.sorting.oop.quicksort import QuickSort

# Test the algorithms
if __name__ == '__main__':
    quick_sort = QuickSort()
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = quick_sort.sort(arr)
    print("QuickSort Sorted array:", sorted_arr)

    merge_sort = MergeSort()
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort.sort(arr)
    print("MergeSort Sorted array:", sorted_arr)

