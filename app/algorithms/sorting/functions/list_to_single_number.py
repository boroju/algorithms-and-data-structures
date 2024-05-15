from typing import List


def list_to_single_number(nums: List[int]) -> int:
    # Convert each number to a string and concatenate them
    concatenated = ''.join(map(str, nums))
    # Convert the concatenated string back to an integer
    single_number = int(concatenated)
    return single_number


if __name__ == "__main__":
    nums = [123, 456, 789]
    result = list_to_single_number(nums)
    print(result)  # Output: 123456789
