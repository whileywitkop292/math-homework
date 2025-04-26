def find_largest_number(numbers):
    """
    Find and return the largest number in a given list of numbers.
    
    Example usage:
    >>> find_largest_number([10, -2, 3, 5, 9])
    10
    >>> find_largest_number([7, 8, 5, 6, 4])
    8
    """
    return max(numbers)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
