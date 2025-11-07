from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional['ListNode'] = None


def append(head: Optional[ListNode], val: int) -> ListNode:
    """Add value to end of list and return head."""
    new_node = ListNode(val)
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def prepend(head: Optional[ListNode], val: int) -> ListNode:
    """Add value to beginning of list and return head."""
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def find(head: Optional[ListNode], val: int) -> bool:
    """Check if value exists in list."""
    current = head
    while current:
        if current.val == val:
            return True
        current = current.next
    return False


def delete(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Delete first occurrence of value and return head."""
    if head is None:
        return None
    
    if head.val == val:
        return head.next
    
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            return head
        current = current.next
    return head


def to_list(head: Optional[ListNode]) -> list:
    """Convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    head = None
    head = append(head, 1)
    head = append(head, 2)
    head = append(head, 3)
    head = prepend(head, 0)
    
    print(f"List: {to_list(head)}")  # [0, 1, 2, 3]
    print(f"Find 2: {find(head, 2)}")  # True
    print(f"Find 5: {find(head, 5)}")  # False
    
    head = delete(head, 2)
    print(f"After delete 2: {to_list(head)}")  # [0, 1, 3]

