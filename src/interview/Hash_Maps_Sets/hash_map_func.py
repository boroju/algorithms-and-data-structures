from typing import Any, Optional, List, Dict, Tuple


def create_hash_map(capacity: int = 16) -> Dict[int, List[Tuple[str, any]]]:
    """Create an empty hash map."""
    return {i: [] for i in range(capacity)}


def hash_key(key: str, capacity: int) -> int:
    """Hash function to get bucket index."""
    return hash(key) % capacity


def put(hm: Dict[int, List[Tuple[str, any]]], key: str, value: any, capacity: int) -> None:
    """Insert or update key-value pair."""
    index = hash_key(key, capacity)
    bucket = hm[index]
    
    # Check if key exists, update if found
    for i, (k, v) in enumerate[Tuple[str, Any]](bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    
    # Key doesn't exist, add new
    bucket.append((key, value))


def get(hm: Dict[int, List[Tuple[str, any]]], key: str, capacity: int) -> Optional[any]:
    """Get value by key."""
    index = hash_key(key, capacity)
    bucket = hm[index]
    
    for k, v in bucket:
        if k == key:
            return v
    return None


def remove(hm: Dict[int, List[Tuple[str, any]]], key: str, capacity: int) -> bool:
    """Remove key-value pair."""
    index = hash_key(key, capacity)
    bucket = hm[index]
    
    for i, (k, v) in enumerate[Tuple[str, Any]](bucket):
        if k == key:
            bucket.pop(i)
            return True
    return False


def contains(hm: Dict[int, List[Tuple[str, any]]], key: str, capacity: int) -> bool:
    """Check if key exists."""
    return get(hm, key, capacity) is not None


def keys(hm: Dict[int, List[Tuple[str, any]]]) -> List[str]:
    """Get all keys."""
    result = []
    for bucket in hm.values():
        for k, v in bucket:
            result.append(k)
    return result


if __name__ == "__main__":
    capacity = 16
    hm = create_hash_map(capacity)
    
    put(hm, "apple", 5, capacity)
    put(hm, "banana", 3, capacity)
    put(hm, "cherry", 8, capacity)
    
    print(f"Get 'apple': {get(hm, 'apple', capacity)}")  # 5
    print(f"Get 'banana': {get(hm, 'banana', capacity)}")  # 3
    print(f"Contains 'cherry': {contains(hm, 'cherry', capacity)}")  # True
    print(f"Contains 'date': {contains(hm, 'date', capacity)}")  # False
    print(f"Keys: {keys(hm)}")  # ['apple', 'banana', 'cherry']
    
    remove(hm, "banana", capacity)
    print(f"After remove 'banana': {contains(hm, 'banana', capacity)}")  # False

