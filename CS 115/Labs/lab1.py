from cs115 import *
import math 

def inverse(n):
    '''Divides 1 over n to get the inverse of n'''
    return 1/n

def e(n):
    '''Approximates the mathematical calue e using a Taylor expansion'''
    list1=range(0,n+1)
    list2=map(math.factorial,list1)
    list3=map(inverse,list2)
    return sum(list3)

def error(n):
    '''Returns the absolute value of the difference between
        the "actual" value of e and the approximation in the e(n) function'''
    return abs(math.e-e(n))
