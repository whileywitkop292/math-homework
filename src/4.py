
import random

def get_random_code():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ["+", "-", "*", "/", "**"]
    operations = ["addition", "subtraction", "multiplication", "division", "exponentiation"]
    equation = ""
    for i in range(random.randint(2, 4)):
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        operation = random.choice(operations)
        symbol = random.choice(symbols)
        equation += f"{num1} {operation} {num2} = "
    return equation