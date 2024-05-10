import unittest
from app.data_structures.queue.poo.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        """
        Initialize a Queue instance for testing.
        """
        self.queue = Queue()

    def test_enqueue(self) -> None:
        """
        Test enqueue operation.
        """
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue(self) -> None:
        """
        Test dequeue operation.
        """
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.size(), 0)

    def test_is_empty(self) -> None:
        """
        Test is_empty method.
        """
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_size(self) -> None:
        """
        Test size method.
        """
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)


if __name__ == '__main__':
    unittest.main()
