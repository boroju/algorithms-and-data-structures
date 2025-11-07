import unittest
from lru_cache_w_exp import LRUCacheWithExpiration
import time


class TestLRUCacheWithExpiration(unittest.TestCase):
    def test_put_and_get(self):
        cache = LRUCacheWithExpiration(3, 5)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)

        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(3), 30)

    def test_expiration(self):
        cache = LRUCacheWithExpiration(3, 5)
        cache.put(1, 10)
        time.sleep(1)
        cache.put(2, 20)
        time.sleep(1)
        cache.put(3, 30)

        # Wait for 5 seconds to exceed max time T for key 1
        # 1 + 1 + 3 = 5 seconds
        time.sleep(3)

        self.assertEqual(cache.get(1), -1)  # Key 1 should be expired
        self.assertEqual(cache.get(2), 20)  # Key 2 should still be valid
        self.assertEqual(cache.get(3), 30)  # Key 3 should still be valid

    def test_eviction_when_full(self):
        cache = LRUCacheWithExpiration(3, 5)
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
