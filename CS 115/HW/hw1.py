''' I pledge my honor that I have abided by the Stevens Honor System - Jonathan Joshua'''

from cs115 import map, reduce

def mult(x, y):
    """Returns the product of xand y"""
    return x * y

def factorial(n):
    """Returns the factorial of n"""
    return reduce(mult, range(1, n+1))

def add(x,y):
    """Returns the sum of two numbers"""
    return x+y

def mean(L):
    """Returns the mean value in that list"""
    return reduce(add, L) / len(L)

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(x):
    """Returns if x is prime or not"""
    if x > 1:
        return sum(map(divides(x), range(2, x))) == 0
    return False

print(map(prime, range(1, 11)))
