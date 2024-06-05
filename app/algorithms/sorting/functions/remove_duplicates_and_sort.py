def remove_duplicates_and_sort(nums):
    # Convert the list to a set to remove duplicates
    unique_nums = set(nums)
    # Convert the set back to a list and sort it
    sorted_nums = sorted(unique_nums)
    return sorted_nums


if __name__ == '__main__':
    # Example usage
    nums = [3, 1, 2, 3, 4, 1, 5]
    print(remove_duplicates_and_sort(nums))  # Output: [1, 2, 3, 4, 5]