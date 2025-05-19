# This is a simple program that checks if a given number is even or odd.
# The program takes an integer input and prints whether it's even or odd.

num = int(input("Enter a number: "))  # Prompt user for input

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
