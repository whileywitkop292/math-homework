def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    for i in range(2, n):
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)

    return fib_seq

n = int(input("Enter the number of terms: "))
fibonacci_sequence = fibonacci(n)
print(f"The Fibonacci sequence up to {n} terms is:")
for num in fibonacci_sequence:
    print(num, end=" ")
