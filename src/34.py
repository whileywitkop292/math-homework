def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    sqrt = (num + 1) // 2  # Use Babylonian method for square root
    return sqrt

# Example usage: print(square_root(4))
