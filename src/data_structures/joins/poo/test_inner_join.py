import unittest
from app.data_structures.joins.poo.inner_join import InnerJoin


class TestInnerJoin(unittest.TestCase):
    def setUp(self):
        # Example data
        self.array1 = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
            {"id": 3, "name": "Charlie", "age": 35}
        ]
        self.array2 = [
            {"id": 1, "city": "New York"},
            {"id": 2, "city": "Los Angeles"},
            {"id": 4, "city": "Chicago"}
        ]
        self.inner_join_instance = InnerJoin(self.array1, self.array2)

    def test_inner_join_empty_arrays(self):
        """
        Test inner join with empty arrays.
        """
        empty_array = []
        inner_join_instance = InnerJoin(empty_array, empty_array)
        result = inner_join_instance.inner_join("id")
        self.assertEqual(result, [])

    def test_inner_join_no_common_key(self):
        """
        Test inner join with arrays having no common key.
        """
        arr1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        arr2 = [{"city": "New York"}, {"city": "Los Angeles"}]
        inner_join_instance = InnerJoin(arr1, arr2)
        result = inner_join_instance.inner_join("city")  # Using a non-common key
        self.assertEqual(result, [])

    def test_inner_join_single_common_key(self):
        """
        Test inner join with arrays having a single common key.
        """
        expected_result = [
            {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
            {"id": 2, "name": "Bob", "age": 25, "city": "Los Angeles"}
        ]
        result = self.inner_join_instance.inner_join("id")
        self.assertEqual(result, expected_result)

    def test_inner_join_multiple_common_keys(self):
        """
        Test inner join with arrays having multiple common keys.
        """
        array1 = [{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]
        array2 = [{"id": 1, "city": "New York", "age": 30}, {"id": 2, "city": "Los Angeles", "age": 25}]
        expected_result = [
            {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
            {"id": 2, "name": "Bob", "age": 25, "city": "Los Angeles"}
        ]
        inner_join_instance = InnerJoin(array1, array2)
        result = inner_join_instance.inner_join("id")
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
