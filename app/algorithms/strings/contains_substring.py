def contains_substring(string, substring):
    """
    Check if the given string contains the substring.

    Args:
        string (str): The main string.
        substring (str): The substring to check for.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    return substring in string


def contains_substring_permutation(string, substring):
    """
    Check if the given string contains the substring even if the characters are in a different order.

    Args:
        string (str): The main string.
        substring (str): The substring to check for.

    Returns:
        bool: True if the substring (or its permutation) is found, False otherwise.
    """
    # Count occurrences of each character in substring
    substring_count = {}
    for char in substring:
        substring_count[char] = substring_count.get(char, 0) + 1

    # Iterate through the string in windows of substring length
    for i in range(len(string) - len(substring) + 1):
        window = string[i:i + len(substring)]
        window_count = {}
        # Count occurrences of each character in the window
        for char in window:
            window_count[char] = window_count.get(char, 0) + 1
        # Check if window contains the same characters as substring
        print("Window:", window)
        print("Window Count:", window_count)
        print("Substring Count:", substring_count)
        if window_count == substring_count:
            return True
    return False


# Example usage:
if __name__ == "__main__":
    string = "hello world"
    substring = "world"
    print("Does string contain substring (as is)?", contains_substring(string, substring))  # Output: True
    substring_v2 = "owrld"
    print("Does string contain substring (permutation)?", contains_substring_permutation(string, substring_v2))  # Output: True
