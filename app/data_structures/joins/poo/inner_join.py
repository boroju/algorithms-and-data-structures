from typing import List, Dict


class InnerJoin:
    def __init__(self, arr1: List[Dict[str, int]], arr2: List[Dict[str, int]]):
        self.arr1 = arr1
        self.arr2 = arr2

    def inner_join(self, key: str) -> List[Dict[str, int]]:
        """
        Performs inner join on two arrays of dictionaries based on a common key.

        Args:
            key (str): The common key to perform the join operation.

        Returns:
            List[Dict[str, int]]: The result of the inner join.
        """
        result = []

        # Check if the key exists in both arrays
        if not all(key in item for item in self.arr1) or not all(key in item for item in self.arr2):
            return result

        # Creating the lookup table (lookup) takes O(n) time, where n is the number of elements in the second array (arr2).
        lookup = {item[key]: item for item in self.arr2}
        # Iterating through the first array (arr1) takes O(m) time, where m is the number of elements in the first array.
        for item in self.arr1:
            # Checking for the common key in the lookup table takes O(1) time.
            if item[key] in lookup:
                result.append({**item, **lookup[item[key]]})

        # Thus, the overall time complexity of the inner_join function is O(n + m),
        # where n is the size of the second array and m is the size of the first array.
        # This implementation is efficient for small to moderate-sized datasets. However, if the datasets are very large,
        # the current implementation may not be the most efficient, especially in terms of memory usage.

        return result


# Test the inner join function
if __name__ == "__main__":
    # Example data
    array1 = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
    array2 = [
        {"id": 1, "city": "New York"},
        {"id": 2, "city": "Los Angeles"},
        {"id": 4, "city": "Chicago"}
    ]

    # Create an instance of InnerJoin
    inner_join_instance = InnerJoin(array1, array2)

    # Perform inner join on 'id' key
    result = inner_join_instance.inner_join("id")
    print("Inner Join Result:")
    for item in result:
        print(item)
