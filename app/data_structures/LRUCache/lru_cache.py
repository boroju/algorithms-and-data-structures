class ListNode:
    """A class to represent a node in the doubly linked list."""

    def __init__(self, key=None, value=None):
        """Initialize a ListNode with key, value, and pointers to prev and next nodes."""
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """A class to represent an LRU Cache."""

    def __init__(self, capacity: int):
        """
        Initialize the LRU Cache with the given capacity.

        Args:
            capacity (int): The maximum capacity of the cache.
        """
        self.capacity = capacity
        self.cache = {}  # Hashtable to store key-node mappings
        # Dummy head and tail nodes for the doubly linked list
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Connect tail to head

    def _move_to_front(self, node):
        """
        Move a given node to the front of the linked list.

        Args:
            node (ListNode): The node to be moved to the front.
        """
        # Remove the node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev
        # Move the node to the front
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Retrieve the value corresponding to the given key from the cache.

        If the key is found, move the accessed node to the front of the list.

        Args:
            key (int): The key of the item to retrieve.

        Returns:
            int: The value corresponding to the key, or -1 if key not found.
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair in the cache.

        If the key already exists, update the value and move the node to the front.
        If the cache is at full capacity, evict the least recently used item before insertion.

        Args:
            key (int): The key of the item to insert/update.
            value (int): The value corresponding to the key.
        """
        if key in self.cache:
            # Update the value and move the node to the front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item (the tail node)
                del_key = self.tail.prev.key
                del self.cache[del_key]
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
            # Add new node to the front
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node


if __name__ == "__main__":
    # Initialize the LRUCache with capacity 5
    cache = LRUCache(5)

    print("Action: put(1, 1)")
    cache.put(1, 1)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(2, 3)")
    cache.put(2, 3)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(3, 4)")
    cache.put(3, 4)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(4, 7)")
    cache.put(4, 7)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(6, 10)")
    cache.put(6, 10)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: get(1)")
    print("Output: ", cache.get(1))
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: get(3)")
    print("Output: ", cache.get(3))
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(1, 5)")
    cache.put(1, 5)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(12, 7)")
    cache.put(12, 7)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(5, 2)")
    cache.put(5, 2)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: get(4)")
    print("Output: ", cache.get(4))
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")
