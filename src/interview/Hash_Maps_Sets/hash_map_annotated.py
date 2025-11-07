from typing import Optional, List, Tuple, Any


class HashMap:
    """
    Hash Map (Hash Table) implementation using chaining for collision resolution.
    
    Hash Map stores key-value pairs and provides O(1) average time complexity
    for insert, search, and delete operations.
    
    How it works:
    1. Hash function converts key to bucket index
    2. Each bucket is a list (chain) to handle collisions
    3. Keys are stored with their values in tuples
    
    Time Complexity:
    - Put: O(1) average, O(n) worst case (all keys hash to same bucket)
    - Get: O(1) average, O(n) worst case
    - Remove: O(1) average, O(n) worst case
    - Contains: O(1) average, O(n) worst case
    
    Space Complexity:
    - O(n) where n is number of key-value pairs
    
    ═══════════════════════════════════════════════════════════════
    🎯 WHEN TO USE HASH MAP vs WHEN NOT TO USE HASH MAP
    ═══════════════════════════════════════════════════════════════
    
    ✅ USE HASH MAP WHEN:
    
    1. Need O(1) Average Lookups
       Use Case: User session cache
       Example: Looking up user session by session ID
       - Hash Map: O(1) average lookup
       - Array: O(n) to search
       - BST: O(log n) lookup
       - Winner: Hash Map ✅
    
    2. No Ordering Needed
       Use Case: Word frequency counter
       Example: Counting occurrences of words in text
       - Hash Map: O(1) insert/update, no ordering overhead
       - BST: O(log n) insert, maintains order you don't need
       - Winner: Hash Map ✅
    
    3. Key-Value Storage
       Use Case: Configuration settings
       Example: Storing app settings by key
       - Hash Map: Natural key-value structure
       - Array: Need to search for key
       - Winner: Hash Map ✅
    
    4. Caching Systems
       Use Case: Web cache, memoization
       Example: Caching API responses by URL
       - Hash Map: Fast O(1) lookups
       - Array: Slow O(n) lookups
       - Winner: Hash Map ✅
    
    5. Counting Frequencies
       Use Case: Character/word counting
       Example: Count character frequencies in string
       - Hash Map: O(1) update per character
       - Array: Need to search first
       - Winner: Hash Map ✅
    
    ❌ DON'T USE HASH MAP WHEN:
    
    1. Need Sorted Order → Use BST Instead
       Use Case: Leaderboard system
       Example: Need to display scores in sorted order
       - Hash Map: No ordering, need to sort (O(n log n))
       - BST: Maintains sorted order automatically
       - Winner: BST ✅
    
    2. Need Range Queries → Use BST Instead
       Use Case: Calendar application
       Example: Find all events between two dates
       - Hash Map: Must check every entry (O(n))
       - BST: Efficient range queries (O(log n + k))
       - Winner: BST ✅
    
    3. Need Index-Based Access → Use Array Instead
       Use Case: Image pixel data
       Example: Accessing pixel at [x][y]
       - Hash Map: Can't access by index
       - Array: O(1) access by index
       - Winner: Array ✅
    
    4. Very Small Dataset (< 10 items) → Use Array Instead
       Use Case: Small fixed-size data
       Example: Storing 5 configuration values
       - Hash Map: Overhead not worth it
       - Array: Simpler, fast enough
       - Winner: Array ✅
    
    5. Need Duplicate Keys → Use MultiMap Instead
       Use Case: One-to-many relationships
       Example: Student to courses mapping
       - Hash Map: Can't store duplicate keys
       - MultiMap: Allows multiple values per key
       - Winner: MultiMap ✅
    
    ═══════════════════════════════════════════════════════════════
    💡 REAL-WORLD EXAMPLES
    ═══════════════════════════════════════════════════════════════
    
    ✅ HASH MAP IS USED IN:
    - Python's dict, JavaScript's Map/Object
    - Database indexes (hash indexes)
    - Caching systems (Redis, Memcached)
    - Session storage (web applications)
    - Counting frequencies (character/word counts)
    - Symbol tables (compilers)
    - Configuration management
    
    ❌ HASH MAP IS NOT USED IN:
    - Sorted data → BST/TreeMap
    - Range queries → BST
    - Priority queues → Heap
    - Sequential access → Array/List
    """
    
    def __init__(self, capacity: int = 16):
        """
        Initialize hash map with given capacity.
        
        Args:
            capacity: Number of buckets (default: 16)
        """
        self.capacity = capacity
        self.size = 0
        # Each bucket is a list of (key, value) tuples
        self.buckets: List[List[Tuple[str, Any]]] = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """
        Hash function to convert key to bucket index.
        
        Uses Python's built-in hash() function and modulo operation
        to map key to a bucket index.
        
        Args:
            key: The key to hash
            
        Returns:
            Bucket index (0 to capacity-1)
        """
        return hash(key) % self.capacity
    
    def put(self, key: str, value: Any) -> None:
        """
        Insert or update key-value pair.
        
        If key exists, updates the value.
        If key doesn't exist, adds new key-value pair.
        
        Time Complexity: O(1) average, O(n) worst case
        
        Args:
            key: The key
            value: The value to store
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key exists in bucket, update if found
        for i, (k, v) in enumerate[Tuple[str, Any]](bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Key doesn't exist, add new key-value pair
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value by key.
        
        Time Complexity: O(1) average, O(n) worst case
        
        Args:
            key: The key to look up
            
        Returns:
            The value if key exists, None otherwise
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Search in bucket for the key
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key: str) -> bool:
        """
        Remove key-value pair.
        
        Time Complexity: O(1) average, O(n) worst case
        
        Args:
            key: The key to remove
            
        Returns:
            True if key was removed, False if key doesn't exist
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Find and remove key from bucket
        for i, (k, v) in enumerate[Tuple[str, Any]](bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
    
    def contains(self, key: str) -> bool:
        """
        Check if key exists in hash map.
        
        Time Complexity: O(1) average, O(n) worst case
        
        Args:
            key: The key to check
            
        Returns:
            True if key exists, False otherwise
        """
        return self.get(key) is not None
    
    def keys(self) -> List[str]:
        """
        Get all keys in the hash map.
        
        Time Complexity: O(n) where n is number of key-value pairs
        
        Returns:
            List of all keys
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)
        return result
    
    def values(self) -> List[Any]:
        """
        Get all values in the hash map.
        
        Time Complexity: O(n) where n is number of key-value pairs
        
        Returns:
            List of all values
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(v)
        return result
    
    def items(self) -> List[Tuple[str, Any]]:
        """
        Get all key-value pairs.
        
        Time Complexity: O(n) where n is number of key-value pairs
        
        Returns:
            List of (key, value) tuples
        """
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result


# Example usage and testing
if __name__ == "__main__":
    print("="*70)
    print("HASH MAP DEMONSTRATION")
    print("="*70)
    
    # Create hash map
    hm = HashMap()
    
    # Insert key-value pairs
    print("\n=== Inserting key-value pairs ===")
    hm.put("apple", 5)
    hm.put("banana", 3)
    hm.put("cherry", 8)
    hm.put("date", 2)
    print(f"Size: {hm.size}")
    
    # Get values
    print("\n=== Getting values ===")
    print(f"Get 'apple': {hm.get('apple')}")  # 5
    print(f"Get 'banana': {hm.get('banana')}")  # 3
    print(f"Get 'cherry': {hm.get('cherry')}")  # 8
    print(f"Get 'nonexistent': {hm.get('nonexistent')}")  # None
    
    # Check existence
    print("\n=== Checking existence ===")
    print(f"Contains 'date': {hm.contains('date')}")  # True
    print(f"Contains 'elderberry': {hm.contains('elderberry')}")  # False
    
    # Update existing key
    print("\n=== Updating existing key ===")
    hm.put("apple", 10)  # Update apple from 5 to 10
    print(f"Get 'apple' after update: {hm.get('apple')}")  # 10
    print(f"Size after update: {hm.size}")  # Still 4 (no new key added)
    
    # Get all keys and values
    print("\n=== All keys and values ===")
    print(f"Keys: {hm.keys()}")
    print(f"Values: {hm.values()}")
    print(f"Items: {hm.items()}")
    
    # Remove key
    print("\n=== Removing key ===")
    print(f"Remove 'banana': {hm.remove('banana')}")  # True
    print(f"Contains 'banana' after remove: {hm.contains('banana')}")  # False
    print(f"Size after remove: {hm.size}")  # 3
    
    print("\n=== Final state ===")
    print(f"Keys: {hm.keys()}")
    print(f"Size: {hm.size}")

