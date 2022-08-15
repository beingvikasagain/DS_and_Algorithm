# import sys
# sys.setrecursionlimit(10000)

def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be integers only!'
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(4))


def fibonacci(n):
    assert n >=0 and int(n) == n, 'The number must be positive integer only'
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))