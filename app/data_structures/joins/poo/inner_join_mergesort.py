from typing import List, Dict
from app.algorithms.sorting.oop.mergesort import MergeSort


class InnerJoinMergeSort:
    def __init__(self, arr1: List[Dict[str, int]], arr2: List[Dict[str, int]]):
        self.arr1 = arr1
        self.arr2 = arr2
        self.merge_sort = MergeSort()  # Initialize MergeSort instance

    # O(n1log(n1) + n2log(n2))
    def inner_join(self, key: str) -> List[Dict[str, int]]:
        """
        Performs inner join on two arrays of dictionaries based on a common key.

        Args:
            key (str): The common key to perform the join operation.

        Returns:
            List[Dict[str, int]]: The result of the inner join.
        """
        # Check if the key exists in any dictionary in arr1 or arr2
        if not any(key in d for d in self.arr1) or not any(key in d for d in self.arr2):
            return []  # If key not found in any dictionary, return an empty list

        # Sort both arrays based on the common key using MergeSort
        self.arr1 = self.merge_sort.sort(self.arr1, key=lambda x: x[key])
        self.arr2 = self.merge_sort.sort(self.arr2, key=lambda x: x[key])

        result = []
        idx1 = idx2 = 0

        while idx1 < len(self.arr1) and idx2 < len(self.arr2):
            if self.arr1[idx1][key] == self.arr2[idx2][key]:
                result.append({**self.arr1[idx1], **self.arr2[idx2]})
                idx1 += 1
                idx2 += 1
            elif self.arr1[idx1][key] < self.arr2[idx2][key]:
                idx1 += 1
            else:
                idx2 += 1

        return result


# Sorting both arrays using MergeSort:
# The time complexity of MergeSort is O(n*log(n)), where n is the number of elements in the array.
# Since we sort both arr1 and arr2 separately, the total time complexity for sorting is O(n1log(n1) + n2log(n2)),
# ----where n1 is the number of elements in arr1 and n2 is the number of elements in arr2.

# Performing the inner join operation:
# After sorting, we iterate through both sorted arrays once to perform the inner join operation.
# The time complexity for performing the inner join operation is O(n1 + n2), where n1 and n2 are the sizes of the sorted arrays.
# Combining both steps, the overall time complexity of the enhanced InnerJoin class is O(n1log(n1) + n2log(n2)) + O(n1 + n2).
# ---However, in Big O notation, we can drop the lower-order terms and constant factors, so the final time complexity can be simplified to O(n1log(n1) + n2log(n2)).
# This implementation is more efficient for larger datasets compared to the previous implementation, especially in terms of time complexity.


if __name__ == "__main__":
    # Example data
    arr1 = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    arr2 = [
        {"id": 1, "city": "New York"},
        {"id": 2, "city": "Los Angeles"},
        {"id": 4, "city": "Chicago"}
    ]

    # Instantiate the InnerJoinMergeSort class with the example data
    inner_join_instance = InnerJoinMergeSort(arr1, arr2)

    # Perform the inner join operation on the "id" key
    result = inner_join_instance.inner_join("id")

    # Print the result
    print("Inner Join Result:")
    for item in result:
        print(item)
