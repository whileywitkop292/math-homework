def solve_math_equation(a, b, c):
    """
    Solves a quadratic equation: ax^2 + bx + c = 0

    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        float: The solution for the given quadratic equation
    """
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real solutions"

# Example usage
a = 1.5
b = 3
c = 2

solution = solve_math_equation(a, b, c)
print("The solution is: ", solution)
