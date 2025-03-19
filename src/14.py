import random

def get_random_math_expression(variables):
    """
    Generates a random math expression using the given variables.
    """
    # List of all possible operators
    operators = ['+', '-', '*', '/']

    # List of all possible values for each variable
    values = [random.randint(1, 10) for i in range(len(variables))]

    # Initialize the expression string
    expression = ''

    # Add the first value to the expression
    expression += str(values[0])

    # Add the operator and the second value to the expression
    expression += operators[random.randint(0, len(operators) - 1)] + str(values[1])

    # Keep adding variables and values until all variables are used up
    for i in range(2, len(variables)):
        expression += operators[random.randint(0, len(operators) - 1)] + str(values[i])

    return expression