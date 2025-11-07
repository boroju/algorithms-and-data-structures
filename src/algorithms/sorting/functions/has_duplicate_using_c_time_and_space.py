from typing import List


# To determine if an array from 0 to n has a duplicate using constant time and space,
# we can utilize Floyd's Tortoise and Hare (Cycle Detection) algorithm.
# This algorithm is also known as the "fast and slow pointers" technique. Here's how it works:
#
# 1. We start with two pointers, often referred to as "slow" and "fast".
# 2. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# 3. If there's a cycle in the array (i.e., a duplicate), eventually, the fast pointer will catch up to the slow pointer.

def has_duplicate(nums: List[int]) -> bool:
    # Initialize slow and fast pointers
    slow = nums[0]
    fast = nums[0]

    # Move pointers until they meet or fast pointer reaches the end
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset one pointer to the start
    slow = nums[0]

    # Move both pointers at the same speed until they meet
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # If slow and fast pointers meet, there's a duplicate
    return slow != nums[0]


if __name__ == "__main__":

    # Example
    nums = [1, 2, 3, 4, 5, 6, 3] # Duplicate 3
    result = has_duplicate(nums)
    print(result)  # Output: True

    # Example
    nums = [1, 2, 3, 4, 5, 6, 0] # No duplicate
    result = has_duplicate(nums)
    print(result)  # Output: True
