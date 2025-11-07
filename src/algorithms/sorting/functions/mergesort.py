from typing import List


# Merge sort is an efficient sorting algorithm with a time complexity of O(n*log(n)).
# It divides the array into halves, recursively sorts each half, and then merges the sorted halves together.
# This results in a sorted array with minimal time complexity, making merge sort suitable for various sorting tasks.
def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array in non-decreasing order using the merge sort algorithm.

    Args:
        arr (List[int]): The input array to be sorted.

    Returns:
        List[int]: The sorted array.
    """
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left (List[int]): The left sorted array.
        right (List[int]): The right sorted array.

    Returns:
        List[int]: The merged sorted array.
    """
    merged = []
    left_index, right_index = 0, 0

    # Merge the two sorted arrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left array
    merged.extend(left[left_index:])

    # Add any remaining elements from the right array
    merged.extend(right[right_index:])

    return merged

# Merge sort is a divide-and-conquer algorithm that works by recursively dividing the array into smaller subarrays,
# sorting each subarray, and then merging them back together to produce the final sorted array.

# The key to merge sort is the merge operation, which combines two sorted arrays into a single sorted array.

# The time complexity of merge sort is O(n*log(n)), where "n" represents the number of elements in the array.

# This time complexity arises because merge sort recursively divides the array into halves until
# each subarray contains only one element (log(n) divisions),
# and then it merges the sorted subarrays together (O(n) time for each merge operation).

# Due to its consistent O(n*log(n)) time complexity, merge sort is efficient for sorting large datasets.
