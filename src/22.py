import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def get_digits_sum(n):
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)
    return digit_sum

n = 100
result = find_factorial(n)
print(result)
print(get_digits_sum(n))
