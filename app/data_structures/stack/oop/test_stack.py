import unittest
from app.data_structures.stack.oop.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initialize a Stack instance for testing.
        """
        self.stack = Stack()

    def test_push(self) -> None:
        """
        Test push operation.
        """
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)

    def test_pop(self) -> None:
        """
        Test pop operation.
        """
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)

    def test_peek(self) -> None:
        """
        Test peek method.
        """
        self.assertIsNone(self.stack.peek())
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_is_empty(self) -> None:
        """
        Test is_empty method.
        """
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self) -> None:
        """
        Test size method.
        """
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
