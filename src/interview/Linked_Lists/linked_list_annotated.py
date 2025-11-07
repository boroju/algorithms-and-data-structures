from typing import Optional, List


class ListNode:
    """
    A node in a Linked List.
    
    Each node contains:
    - val: The value stored in the node
    - next: Pointer to the next node (None if last node)
    """
    
    def __init__(self, val: int):
        self.val = val
        self.next: Optional['ListNode'] = None


class LinkedList:
    """
    Singly Linked List implementation.
    
    A linked list is a linear data structure where elements are stored in nodes,
    and each node points to the next node. Unlike arrays, elements are not stored
    in contiguous memory locations.
    
    Structure:
    head -> [val1] -> [val2] -> [val3] -> None
    
    Time Complexity:
    - Append: O(n) - must traverse to end
    - Prepend: O(1) - add at head
    - Find: O(n) - must traverse list
    - Delete: O(n) - must find node first
    - Access by index: O(n) - must traverse to index
    
    Space Complexity:
    - O(n) where n is number of nodes
    
    ═══════════════════════════════════════════════════════════════
    🎯 WHEN TO USE LINKED LIST vs WHEN NOT TO USE LINKED LIST
    ═══════════════════════════════════════════════════════════════
    
    ✅ USE LINKED LIST WHEN:
    
    1. Frequent Insertions/Deletions at Beginning
       Use Case: Stack implementation, undo/redo operations
       Example: Adding items to undo stack
       - Linked List: O(1) prepend
       - Array: O(n) shift all elements
       - Winner: Linked List ✅
    
    2. Dynamic Size (Unknown Size)
       Use Case: Reading data of unknown length
       Example: Reading file line by line, building list
       - Linked List: Grows dynamically, no resizing needed
       - Array: May need to resize (copy all elements)
       - Winner: Linked List ✅
    
    3. Memory Efficiency (Sparse Data)
       Use Case: Sparse matrices, polynomial representation
       Example: Storing only non-zero coefficients
       - Linked List: Only stores what's needed
       - Array: Wastes space for zeros
       - Winner: Linked List ✅
    
    4. No Random Access Needed
       Use Case: Queue implementation, processing sequences
       Example: Task queue, message queue
       - Linked List: Sequential access is fine
       - Array: Random access not needed
       - Winner: Linked List ✅ (simpler than array)
    
    5. Implementing Other Data Structures
       Use Case: Stack, Queue, Deque
       Example: Stack with push/pop at head
       - Linked List: Natural fit for stack/queue
       - Array: Works but less intuitive
       - Winner: Linked List ✅
    
    ❌ DON'T USE LINKED LIST WHEN:
    
    1. Need Random Access → Use Array Instead
       Use Case: Accessing element at index i
       Example: arr[i] = value
       - Linked List: O(n) to access index i
       - Array: O(1) direct access
       - Winner: Array ✅
    
    2. Need Fast Search → Use Hash Map or BST Instead
       Use Case: Finding specific value
       Example: Search for user by ID
       - Linked List: O(n) linear search
       - Hash Map: O(1) average lookup
       - BST: O(log n) lookup
       - Winner: Hash Map/BST ✅
    
    3. Memory Overhead Matters → Use Array Instead
       Use Case: Large datasets, memory-constrained systems
       Example: Storing 1M integers
       - Linked List: Extra memory for pointers (2x overhead)
       - Array: Only data, no pointers
       - Winner: Array ✅
    
    4. Cache Performance Matters → Use Array Instead
       Use Case: Performance-critical code
       Example: Numerical computations
       - Linked List: Non-contiguous memory, poor cache locality
       - Array: Contiguous memory, good cache performance
       - Winner: Array ✅
    
    5. Need to Sort Frequently → Use Array Instead
       Use Case: Maintaining sorted data
       Example: Sorted list of scores
       - Linked List: Hard to sort, O(n²) or complex
       - Array: Easy to sort, O(n log n)
       - Winner: Array ✅
    
    ═══════════════════════════════════════════════════════════════
    💡 REAL-WORLD EXAMPLES
    ═══════════════════════════════════════════════════════════════
    
    ✅ LINKED LIST IS USED IN:
    - Stack implementation (push/pop at head)
    - Queue implementation (enqueue at tail, dequeue at head)
    - Undo/redo functionality (browser history, text editor)
    - Polynomial representation (sparse polynomials)
    - Graph adjacency lists
    - Memory allocators (free list management)
    - Browser back/forward buttons
    
    ❌ LINKED LIST IS NOT USED IN:
    - Random access → Array
    - Fast search → Hash Map/BST
    - Numerical computations → Array (cache performance)
    - Sorted data → Array/BST
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None
    
    def append(self, val: int) -> None:
        """
        Add value to end of list.
        
        Time Complexity: O(n) - must traverse to end
        Space Complexity: O(1)
        
        Args:
            val: Value to add
        """
        new_node = ListNode(val)
        
        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to end and add new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, val: int) -> None:
        """
        Add value to beginning of list.
        
        Time Complexity: O(1) - constant time
        Space Complexity: O(1)
        
        Args:
            val: Value to add
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, val: int) -> bool:
        """
        Check if value exists in list.
        
        Time Complexity: O(n) - must traverse list
        Space Complexity: O(1)
        
        Args:
            val: Value to search for
            
        Returns:
            True if value exists, False otherwise
        """
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def delete(self, val: int) -> bool:
        """
        Delete first occurrence of value.
        
        Time Complexity: O(n) - must find node first
        Space Complexity: O(1)
        
        Args:
            val: Value to delete
            
        Returns:
            True if value was deleted, False if not found
        """
        if self.head is None:
            return False
        
        # If head is the node to delete
        if self.head.val == val:
            self.head = self.head.next
            return True
        
        # Search for node to delete
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def get(self, index: int) -> Optional[int]:
        """
        Get value at given index.
        
        Time Complexity: O(n) - must traverse to index
        Space Complexity: O(1)
        
        Args:
            index: Index of value to get
            
        Returns:
            Value at index, or None if index out of bounds
        """
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return None
    
    def size(self) -> int:
        """
        Get number of nodes in list.
        
        Time Complexity: O(n) - must traverse entire list
        Space Complexity: O(1)
        
        Returns:
            Number of nodes
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def to_list(self) -> List[int]:
        """
        Convert linked list to Python list.
        
        Time Complexity: O(n)
        Space Complexity: O(n) for result list
        
        Returns:
            List of values
        """
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev


# Example usage and testing
if __name__ == "__main__":
    print("="*70)
    print("LINKED LIST DEMONSTRATION")
    print("="*70)
    
    # Create linked list
    ll = LinkedList()
    
    # Append values
    print("\n=== Appending values ===")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"List: {ll.to_list()}")  # [1, 2, 3]
    print(f"Size: {ll.size()}")  # 3
    
    # Prepend value
    print("\n=== Prepending value ===")
    ll.prepend(0)
    print(f"List: {ll.to_list()}")  # [0, 1, 2, 3]
    
    # Find values
    print("\n=== Finding values ===")
    print(f"Find 2: {ll.find(2)}")  # True
    print(f"Find 5: {ll.find(5)}")  # False
    
    # Get by index
    print("\n=== Getting by index ===")
    print(f"Get index 0: {ll.get(0)}")  # 0
    print(f"Get index 2: {ll.get(2)}")  # 2
    print(f"Get index 10: {ll.get(10)}")  # None
    
    # Delete value
    print("\n=== Deleting value ===")
    print(f"Delete 2: {ll.delete(2)}")  # True
    print(f"List: {ll.to_list()}")  # [0, 1, 3]
    print(f"Delete 5: {ll.delete(5)}")  # False
    
    # Reverse list
    print("\n=== Reversing list ===")
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")  # [3, 1, 0]
    
    print("\n=== Final state ===")
    print(f"List: {ll.to_list()}")
    print(f"Size: {ll.size()}")

