from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional['ListNode'] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
    
    def append(self, val: int) -> None:
        """Add value to end of list."""
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, val: int) -> None:
        """Add value to beginning of list."""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, val: int) -> bool:
        """Check if value exists in list."""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def delete(self, val: int) -> bool:
        """Delete first occurrence of value."""
        if self.head is None:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def to_list(self) -> list:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    
    print(f"List: {ll.to_list()}")  # [0, 1, 2, 3]
    print(f"Find 2: {ll.find(2)}")  # True
    print(f"Find 5: {ll.find(5)}")  # False
    
    ll.delete(2)
    print(f"After delete 2: {ll.to_list()}")  # [0, 1, 3]

