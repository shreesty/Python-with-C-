# Recursive function to calculate factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = 10
    print(f"Factorial of {num} is {factorial(num)}")
