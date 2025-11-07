import unittest
from app.algorithms.sorting.oop.mergesort import MergeSort
from app.data_structures.joins.poo.inner_join_mergesort import InnerJoinMergeSort


class TestInnerJoinMergeSort(unittest.TestCase):
    def setUp(self):
        # Example data
        self.arr1 = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
        self.arr2 = [
            {"id": 1, "city": "New York"},
            {"id": 2, "city": "Los Angeles"},
            {"id": 4, "city": "Chicago"}
        ]

        # Initialize InnerJoinMergeSort instance
        self.inner_join_instance = InnerJoinMergeSort(self.arr1, self.arr2)

    def test_inner_join_with_existing_key(self):
        # Test inner join with existing key "id"
        result = self.inner_join_instance.inner_join("id")
        expected_result = [
            {"id": 1, "name": "Alice", "city": "New York"},
            {"id": 2, "name": "Bob", "city": "Los Angeles"}
        ]
        self.assertEqual(result, expected_result)

    def test_inner_join_with_non_existing_key(self):
        # Test inner join with non-existing key "nonexistent_key"
        result = self.inner_join_instance.inner_join("nonexistent_key")
        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
