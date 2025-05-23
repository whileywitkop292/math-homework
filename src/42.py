def add_numbers(a: int, b: int) -> int:
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    return a - b

def multiply_numbers(a: int, b: int) -> int:
    return a * b

def divide_numbers(a: int, b: int) -> float:
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
