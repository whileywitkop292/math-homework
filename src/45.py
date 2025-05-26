# This is an example of a simple program that sums two numbers.
def add_numbers(x, y):
    return x + y

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
