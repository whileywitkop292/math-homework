import math

def calculate_square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    else:
        return math.sqrt(num)

try:
    result = calculate_square_root(16)
except ValueError as e:
    print(e)
