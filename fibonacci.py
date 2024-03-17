import time

# Function to calculate Fibonacci using iteration
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Function to calculate Fibonacci using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Measure rendering time for both approaches
start_time = time.time()
result_iterative = fibonacci_iterative(35)
end_time = time.time()
iterative_time = end_time - start_time

start_time = time.time()
result_recursive = fibonacci_recursive(35)
end_time = time.time()
recursive_time = end_time - start_time

# Print results and rendering times
print(f"Fibonacci using iteration: {result_iterative}")
print(f"Time taken for iteration: {iterative_time:.6f} seconds\n")

print(f"Fibonacci using recursion: {result_recursive}")
print(f"Time taken for recursion: {recursive_time:.6f} seconds")