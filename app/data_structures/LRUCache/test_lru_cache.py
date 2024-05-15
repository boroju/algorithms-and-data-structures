import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_put_and_get(self):
        cache = LRUCache(3)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)

        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(3), 30)

    def test_eviction_when_full(self):
        cache = LRUCache(3)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)

        # Inserting a new item should evict the least recently used item (key=1)
        cache.put(4, 40)

        self.assertEqual(cache.get(1), -1)  # Key 1 should be evicted
        self.assertEqual(cache.get(2), 20)  # Key 2 should still be valid
        self.assertEqual(cache.get(3), 30)  # Key 3 should still be valid
        self.assertEqual(cache.get(4), 40)  # Key 4 should be valid


if __name__ == '__main__':
    unittest.main()
