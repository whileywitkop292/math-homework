def get_random_math_problem(max_num=100):
    """Generates a random math problem as a string."""
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        return f"{num1} + {num2}"
    elif op == "-":
        return f"{num1} - {num2}"
    elif op == "*":
        return f"{num1} * {num2}"
    else:
        return f"{num1} / {num2}"
