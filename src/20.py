def square_and_multiply(number, exponent):
    """
    This function takes two integers: number and exponent.
    It returns the result of squaring (number^exponent) using Python's built-in pow function,
    which is more efficient than using a for loop.

    Parameters:
    - number: an integer
    - exponent: an integer

    Returns:
    - The square of the given number raised to the power of the specified exponent.
    """
    # Using python's pow function for squaring (number^exponent)
    return pow(number, exponent)

# Example usage and verification:
example_number = 3
example_exponent = 5
result = square_and_multiply(example_number, example_exponent)
print(f"{example_number}^{example_exponent} = {result}")
