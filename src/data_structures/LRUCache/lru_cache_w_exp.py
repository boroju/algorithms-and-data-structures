import time
import datetime


class ListNode:
    """A class to represent a node in the doubly linked list."""

    def __init__(self, key=None, value=None):
        """Initialize a ListNode with key, value, and pointers to prev and next nodes."""
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.timestamp = time.time()  # Track the creation time of the node


class LRUCacheWithExpiration:
    """A class to represent an LRU Cache with a maximum time T before removal for each item."""

    def __init__(self, capacity: int, max_time: float):
        """
        Initialize the LRU Cache with the given capacity and maximum time before removal.

        Args:
            capacity (int): The maximum capacity of the cache.
            max_time (float): The maximum time (in seconds) before an item is removed from the cache.
        """
        self.capacity = capacity
        self.max_time = max_time
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

        If the key is found and the item has exceeded the maximum time T, remove it from the cache.

        Args:
            key (int): The key of the item to retrieve.

        Returns:
            int: The value corresponding to the key, or -1 if key not found or item expired.
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Check if the item has exceeded the maximum time T
        if time.time() - node.timestamp > self.max_time:
            # Remove the expired item from the cache
            del self.cache[key]
            self._remove_node(node)
            return -1
        # Move the accessed node to the front
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
                self._remove_node(self.tail.prev)
            # Add new node to the front
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node

    def _remove_node(self, node):
        """
        Remove a given node from the linked list.

        Args:
            node (ListNode): The node to be removed.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

# We introduce a timestamp attribute in the ListNode class to track the creation time of each node.
# In the get method, before returning the value, we check if the item has exceeded the maximum time T. If so, we remove it from the cache and return -1.
# The put method remains the same, but upon insertion of a new node, the timestamp attribute is set to the current time.
# The _remove_node method is added to the LRUCache class to remove a given node from the linked list. This method is used internally when removing expired items from the cache.


if __name__ == "__main__":
    # Create an LRU Cache with capacity 3 and maximum time T of 5 seconds
    cache = LRUCacheWithExpiration(3, 5)

    print("Current time:", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    print("Action: put(1, 10)")
    cache.put(1, 10)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(2, 20)")
    time.sleep(1)
    cache.put(2, 20)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Action: put(3, 30)")
    time.sleep(1)
    cache.put(3, 30)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Retrieve values from the cache:")
    print("Output for key 1:", cache.get(1))  # Output: 10 (within max time T)
    print("Output for key 2:", cache.get(2))  # Output: 20 (within max time T)
    print("Output for key 3:", cache.get(3))  # Output: 30 (within max time T)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Wait for 6 seconds (to exceed max time T for key 1)")
    time.sleep(4)
    print("Current time:", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    print("Retrieve values from the cache again:")
    print("Output for key 1:", cache.get(1))  # Output: -1 (expired, key 1 is removed)
    print("Output for key 2:", cache.get(2))  # Output: 20 (within max time T)
    print("Output for key 3:", cache.get(3))  # Output: 30 (within max time T)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Insert a new key-value pair (4, 40), evicting the least recently used item (key=2)")
    cache.put(4, 40)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Retrieve values from the cache:")
    print("Output for key 2:", cache.get(2))  # Output: -1 (expired, key 2 is removed)
    print("Output for key 3:", cache.get(3))  # Output: 30 (within max time T)
    print("Output for key 4:", cache.get(4))  # Output: 40 (within max time T)
    print("LRU Cache:")
    print({key: (node.key, node.value) for key, node in cache.cache.items()})
    print("-----------------------------------------------------------------")

    print("Current time:", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
