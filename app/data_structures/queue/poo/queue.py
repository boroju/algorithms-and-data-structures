from typing import Any, List


class Queue:
    def __init__(self) -> None:
        """
        Initialize an empty queue.
        """
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.items) == 0

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of the queue.
        """
        self.items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item from the queue.
        """
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items.pop(0)

    def size(self) -> int:
        """
        Return the number of items in the queue.
        """
        return len(self.items)


# The Queue class represents a first-in, first-out (FIFO) data structure.
# It supports two main operations: enqueue, which adds an item to the rear of the queue,
# and dequeue, which removes and returns the front item from the queue.

if __name__ == '__main__':
    # Create a new queue
    queue = Queue()

    # Enqueue items
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Dequeue items
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    print(queue.dequeue())  # Output: 3

    # Check if the queue is empty
    print(queue.is_empty())  # Output: True
