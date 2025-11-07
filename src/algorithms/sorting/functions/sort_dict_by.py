def sort_by_value(data, reverse=False):
    """
      Sorts a dictionary by value in ascending or descending order.

      Args:
          data: A dictionary to be sorted.
          reverse: Boolean flag to sort in descending order (default: False - ascending).

      Returns:
          A list of tuples containing the sorted key-value pairs.
      """
    return sorted(data.items(), key=lambda item: item[1], reverse=reverse)


def sort_by_key(data, reverse=False):
    """
      Sorts a dictionary by key in alphabetical order (ascending or descending).

      Args:
          data: A dictionary to be sorted.
          reverse: Boolean flag to sort in descending order (default: False - ascending).

      Returns:
          A list of tuples containing the sorted key-value pairs.
      """
    return sorted(data.items(), key=lambda item: item[0], reverse=reverse)


if __name__ == '__main__':

    my_dict = {"a": 3, "b": 1, "c": 2}

    # Example usage
    sorted_data = sort_by_value(my_dict)
    print(sorted_data)

    # Example usage with descending order
    my_dict = {"a": 3, "b": 1, "c": 2}
    sorted_data_desc = sort_by_value(my_dict, reverse=True)
    print(sorted_data_desc)

    my_dict = {"c": "Cat", "a": "Apple", "b": "Banana"}

    # Example usage with ascending order
    sorted_data_asc = sort_by_key(my_dict)
    print(sorted_data_asc)

    # Example usage with descending order
    sorted_data_desc = sort_by_key(my_dict, reverse=True)
    print(sorted_data_desc)
