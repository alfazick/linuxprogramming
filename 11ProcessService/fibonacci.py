import sys
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fibonacci.py [n]")
        sys.exit(1)

    n = int(sys.argv[1])
    print(f"Calculating Fibonacci({n})")

    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution Time: {end_time - start_time} seconds")
