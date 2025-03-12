def get_random_number(low=1, high=10):
    return low + (high - low) * random.uniform()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_random_prime(low=1, high=10):
    while True:
        number = get_random_number(low, high)
        if is_prime(number):
            return number
