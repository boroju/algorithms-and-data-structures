from typing import List, Dict


def create_hash_set(capacity: int = 16) -> Dict[int, List[int]]:
    """Create an empty hash set."""
    return {i: [] for i in range(capacity)}


def hash_value(value: int, capacity: int) -> int:
    """Hash function to get bucket index."""
    return hash(value) % capacity


def add(hs: Dict[int, List[int]], value: int, capacity: int) -> None:
    """Add value to set if not present."""
    index = hash_value(value, capacity)
    bucket = hs[index]
    
    if value not in bucket:
        bucket.append(value)


def remove(hs: Dict[int, List[int]], value: int, capacity: int) -> bool:
    """Remove value from set."""
    index = hash_value(value, capacity)
    bucket = hs[index]
    
    if value in bucket:
        bucket.remove(value)
        return True
    return False


def contains(hs: Dict[int, List[int]], value: int, capacity: int) -> bool:
    """Check if value exists in set."""
    index = hash_value(value, capacity)
    return value in hs[index]


def to_list(hs: Dict[int, List[int]]) -> List[int]:
    """Convert set to list."""
    result = []
    for bucket in hs.values():
        result.extend(bucket)
    return result


if __name__ == "__main__":
    capacity = 16
    hs = create_hash_set(capacity)
    
    add(hs, 1, capacity)
    add(hs, 2, capacity)
    add(hs, 3, capacity)
    add(hs, 2, capacity)  # Duplicate, won't add
    
    print(f"Contains 2: {contains(hs, 2, capacity)}")  # True
    print(f"Contains 5: {contains(hs, 5, capacity)}")  # False
    print(f"To list: {to_list(hs)}")  # [1, 2, 3] (order may vary)
    
    remove(hs, 2, capacity)
    print(f"After remove 2: {contains(hs, 2, capacity)}")  # False

