def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib = [0, 1]
    
    # Calculate the remaining Fibonacci numbers
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(5))
