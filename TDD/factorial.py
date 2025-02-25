def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
  
def factorial_refactor(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result