def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    y = x + 1
    while True:
        sqrt_y = (y + x / y) / 2
        if abs(sqrt_y - y) < 0.001:
            return int(sqrt_y)
        else:
            y += 1

# Example usage
try:
    print(square_root(4))  # Output: 2
except ValueError as e:
    print(e)
