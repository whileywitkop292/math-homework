
import random

def get_random_python_code():
    numbers = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    expressions = []
    for i in range(3):
        num1 = random.choice(numbers)
        op = random.choice(operators)
        num2 = random.choice(numbers)
        expressions.append("{} {} {}".format(num1, op, num2))
    return "\n".join(expressions)