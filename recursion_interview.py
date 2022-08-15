# Find the sum of the digits of positive integer using recursion

def sumofDigits(n):
    assert n>=0 and int(n)==n, 'The number has to be positive integer only!'
    if n==0:
        return n
    return int(n%10)+sumofDigits(int(n//10))

print(sumofDigits(11123))


def powerDigits(base, exp):
    assert exp > 0 and int(exp)==exp, 'The exp should be positive integer only!'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * powerDigits(base, exp-1)

print(powerDigits(2,3))

def gcd(a,b):
    assert int(a) == a and int(b) == b, 'The number must be positive integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    
    return gcd(b, a%b)

print(gcd(48,8))

# convert a number from decial to binary unsing recursion

def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be integer!'
    if n == 0:
        return 0
    return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(13))
 