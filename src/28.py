import math
import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_sequence(length):
    sequence = []
    while len(sequence) < length:
        index = random.randint(0, len(sequence) - 1)
        sequence.append(random.choice(["prime", "composite"]))
    return sequence

def find_next_prime(x, y):
    if is_prime(x):
        x = str(int(math.sqrt(x)))
        for i in range(len(x)):
            if int(x[i]) == 1:
                next_num = f"{x[0:i]}{int(x[i] + '5')}"
                return next_num
    elif is_prime(y):
        y = str(int(math.sqrt(y)))
        for i in range(len(y)):
            if int(y[i]) == 1:
                next_num = f"{y[0:i]}{int(y[i] + '5')}"
                return next_num

    raise ValueError("Either x or y cannot be prime numbers.")
