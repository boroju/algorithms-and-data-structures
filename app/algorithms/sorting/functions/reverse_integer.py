# To reverse an integer without converting it to other data types, you can use mathematical operations.

def reverse_integer(x: int) -> int:
    # Initialize the variable to store the reversed number
    reversed_num = 0

    # Flag to indicate if the input integer is negative
    is_negative = False

    # Check if the input integer is negative
    if x < 0:
        is_negative = True
        # If negative, make it positive for reversal
        x = -x

    # Reverse the integer using a loop
    while x != 0:
        # Extract the last digit of the input integer
        digit = x % 10
        # Append the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the input integer
        x //= 10

    # If the input integer was originally negative, make the reversed number negative
    if is_negative:
        reversed_num = -reversed_num

    # Return the reversed integer
    return reversed_num

# This function handles both positive and negative integers.
# It iteratively extracts the digits from the input number and constructs the reversed number.
# Time complexity for this algorithm is O(log10(n)), where n is the input integer.
# This is because the number of iterations in the while loop is proportional to the number of digits in the input integer.


if __name__ == "__main__":

    # Example 1:
    x = 123
    # Output: 321
    print(reverse_integer(x))

    # Example 2:
    x = -123
    # Output: -321
    print(reverse_integer(x))

    # Example 3:
    x = 120
    # Output: 21
    print(reverse_integer(x))

    # Example 4:
    x = 0
    # Output: 0
    print(reverse_integer(x))
