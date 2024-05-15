class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self  # Initialize prev pointer to itself
        self.next = self  # Initialize next pointer to itself

def find_and_fix_broken_node(head):
    # If the list is empty or has only one node, there are no broken nodes
    if not head or head.next == head:
        return None

    # Initialize pointers
    current = head.next
    prev = head

    # Traverse the list
    while current != head:
        # Check for inconsistency
        if prev.next != current or current.prev != prev:
            # Found the broken node
            # Fix the broken link
            prev.next = current
            current.prev = prev
            return current
        # Move to the next nodes
        prev = current
        current = current.next

    # If no broken node is found, return None
    return None


if __name__ == "__main__":
    # Create a circular doubly linked list
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    # Assume node4 is the broken node
    node4.prev = node2  # Incorrect prev pointer
    node4.next = node1  # Incorrect next pointer
    node1.prev = node4  # Incorrect prev pointer

    # Set the head of the list
    head = node1

    # Fix the broken node
    broken_node = find_and_fix_broken_node(head)

    # Print the value of the fixed broken node
    if broken_node:
        print("Broken node found and fixed. Value:", broken_node.val)
    else:
        print("No broken node found.")
