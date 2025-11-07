from collections import deque
from typing import List


class LinkedList:
    def __init__(self):
        self._deque = deque()
    
    def append(self, val: int) -> None:
        """Add value to end of list."""
        self._deque.append(val)
    
    def prepend(self, val: int) -> None:
        """Add value to beginning of list."""
        self._deque.appendleft(val)
    
    def find(self, val: int) -> bool:
        """Check if value exists in list."""
        return val in self._deque
    
    def delete(self, val: int) -> bool:
        """Delete first occurrence of value."""
        try:
            self._deque.remove(val)
            return True
        except ValueError:
            return False
    
    def get(self, index: int) -> int:
        """Get value at given index."""
        return self._deque[index]
    
    def size(self) -> int:
        """Get number of nodes in list."""
        return len(self._deque)
    
    def to_list(self) -> List[int]:
        """Convert linked list to Python list."""
        return list(self._deque)
    
    def reverse(self) -> None:
        """Reverse the linked list in-place."""
        self._deque.reverse()


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    
    print(f"List: {ll.to_list()}")  # [0, 1, 2, 3]
    print(f"Size: {ll.size()}")  # 4
    print(f"Find 2: {ll.find(2)}")  # True
    print(f"Find 5: {ll.find(5)}")  # False
    print(f"Get index 2: {ll.get(2)}")  # 2
    
    ll.delete(2)
    print(f"After delete 2: {ll.to_list()}")  # [0, 1, 3]
    
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")  # [3, 1, 0]

