def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    else:
        return math.sqrt(number)

try:
    print(square_root(16))  # This should output 4.0
except ValueError as e:
    print(e)
