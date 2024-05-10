from typing import List


# The Big O notation for the quicksort algorithm is O(n*log(n)),
# where "n" represents the number of elements in the array.
def quicksort(arr: List[int]):
    """
    Quicksort algorithm implementation.
    arr: List[int] -- the array to be sorted.
    """
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Divide and Conquer: Quicksort is a divide-and-conquer algorithm.
# It repeatedly divides the array into smaller subarrays, sorts each subarray independently,
# and then combines the sorted subarrays to produce the final sorted array.

# Partitioning: In each recursive step, the algorithm partitions the array around a pivot element.
# This partitioning process takes O(n) time, where "n" is the number of elements in the array.

# Recursion: After partitioning, the algorithm recursively sorts the smaller subarrays.
# The time complexity of the recursion is determined by the depth of the recursion tree,
# which is log(n) in the average and best cases.

# Combine: Finally, the algorithm combines the sorted subarrays, which can be done in linear time.

# Worst-case Scenario: In the worst-case scenario, the pivot selection leads to highly unbalanced partitions
