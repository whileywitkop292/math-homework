# Write your mathematical problem here
# Example: solve 2x + 3 = 7
# Replace with actual values or equations as needed

# Solve for x
import sympy as sp

x = sp.symbols('x')
equation = sp.Eq(2*x + 3, 7)
solution = sp.solve(equation, x)

solution
