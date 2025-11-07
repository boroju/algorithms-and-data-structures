from typing import Optional, List, Tuple


class HashMap:
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.size = 0
        self.buckets: List[List[Tuple[str, any]]] = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """Hash function to get bucket index."""
        return hash(key) % self.capacity
    
    def put(self, key: str, value: any) -> None:
        """Insert or update key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key exists, update if found
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist, add new
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key: str) -> Optional[any]:
        """Get value by key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key: str) -> bool:
        """Remove key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
    
    def contains(self, key: str) -> bool:
        """Check if key exists."""
        return self.get(key) is not None
    
    def keys(self) -> List[str]:
        """Get all keys."""
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)
        return result


if __name__ == "__main__":
    hm = HashMap()
    hm.put("apple", 5)
    hm.put("banana", 3)
    hm.put("cherry", 8)
    
    print(f"Get 'apple': {hm.get('apple')}")  # 5
    print(f"Get 'banana': {hm.get('banana')}")  # 3
    print(f"Contains 'cherry': {hm.contains('cherry')}")  # True
    print(f"Contains 'date': {hm.contains('date')}")  # False
    print(f"Keys: {hm.keys()}")  # ['apple', 'banana', 'cherry']
    
    hm.remove("banana")
    print(f"After remove 'banana': {hm.contains('banana')}")  # False

