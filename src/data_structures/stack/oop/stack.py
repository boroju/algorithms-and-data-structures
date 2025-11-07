from typing import Any, List


# The Stack class represents a last-in, first-out (LIFO) data structure.
# It supports three main operations: push, which adds an item to the top of the stack,
# pop, which removes and returns the top item from the stack,
# and peek, which returns the top item from the stack without removing it.
class Stack:
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def peek(self) -> Any:
        """
        Return the top item from the stack without removing it.
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]

    def size(self) -> int:
        """
        Return the number of items in the stack.
        """
        return len(self.items)


# Example usage:
if __name__ == '__main__':
    # Create a new stack
    stack = Stack()

    # Push items
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Pop items
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 1

    # Check if the stack is empty
    print(stack.is_empty())  # Output: True
