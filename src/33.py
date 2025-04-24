def calculate_square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    else:
        return math.sqrt(num)
