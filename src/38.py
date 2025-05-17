def calculate_square_root(num):
    """
    Calculate the square root of a given number.
    
    Args:
        num: A positive number to find the square root of.
    
    Returns:
        The square root of the input number as an integer.
    """
    return int(abs(num) ** 0.5)

# Example usage
result = calculate_square_root(16)
print(f"The square root of {16} is: {result}")
