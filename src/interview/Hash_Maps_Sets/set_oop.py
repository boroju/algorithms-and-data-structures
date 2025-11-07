from typing import List, Set as PySet


class HashSet:
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.size = 0
        self.buckets: List[List[int]] = [[] for _ in range(capacity)]
    
    def _hash(self, value: int) -> int:
        """Hash function to get bucket index."""
        return hash(value) % self.capacity
    
    def add(self, value: int) -> None:
        """Add value to set if not present."""
        index = self._hash(value)
        bucket = self.buckets[index]
        
        if value not in bucket:
            bucket.append(value)
            self.size += 1
    
    def remove(self, value: int) -> bool:
        """Remove value from set."""
        index = self._hash(value)
        bucket = self.buckets[index]
        
        if value in bucket:
            bucket.remove(value)
            self.size -= 1
            return True
        return False
    
    def contains(self, value: int) -> bool:
        """Check if value exists in set."""
        index = self._hash(value)
        return value in self.buckets[index]
    
    def to_list(self) -> List[int]:
        """Convert set to list."""
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result


if __name__ == "__main__":
    s = HashSet()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(2)  # Duplicate, won't add
    
    print(f"Contains 2: {s.contains(2)}")  # True
    print(f"Contains 5: {s.contains(5)}")  # False
    print(f"Size: {s.size}")  # 3
    print(f"To list: {s.to_list()}")  # [1, 2, 3] (order may vary)
    
    s.remove(2)
    print(f"After remove 2: {s.contains(2)}")  # False

