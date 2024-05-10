from typing import List, Callable, Any


class MergeSort:
    def sort(self, arr: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        """
        Sorts a list in non-decreasing order using the mergesort algorithm.

        Args:
            arr (List[Any]): The input list to be sorted.
            key (Callable[[Any], Any]): A function that extracts a comparable value from each element.

        Returns:
            List[Any]: The sorted list.
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.sort(arr[:mid], key)
        right_half = self.sort(arr[mid:], key)

        return self.merge(left_half, right_half, key)

    def merge(self, left: List[Any], right: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        """
        Merges two sorted lists into a single sorted list.

        Args:
            left (List[Any]): The left sorted list.
            right (List[Any]): The right sorted list.
            key (Callable[[Any], Any]): A function that extracts a comparable value from each element.

        Returns:
            List[Any]: The merged sorted list.
        """
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if key(left[left_index]) < key(right[right_index]):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged


if __name__ == "__main__":
    # Example with integers
    arr_integers = [5, 2, 8, 1, 3, 9, 4, 6, 7]
    merge_sort_integers = MergeSort()
    sorted_integers = merge_sort_integers.sort(arr_integers, key=lambda x: x)
    print("Sorted Integers:", sorted_integers)

    # Example with mixed data types
    arr_mixed = [
        {"id": 1, "name": "Alice"},
        {"id": "2", "name": "Bob"},  # Here, id is a string
        {"id": 1, "name": "Charlie"}
    ]
    merge_sort_mixed = MergeSort()

    # Convert string IDs to integers for comparison
    sorted_mixed = merge_sort_mixed.sort(arr_mixed, key=lambda x: int(x["id"]))
    print("Sorted Mixed Data Types:", sorted_mixed)