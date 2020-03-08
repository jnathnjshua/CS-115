''' I pledge my honor that I have abided by the Stevens Honor System. - Jonathan Joshua'''

from cs115 import *

def dot(L, K):
    """Return the dot product of the lists L & K"""
    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """Use string S as an input to return a list of the characters"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    """Return the index at which e is first found in L"""
    if L == []:
        return 0.0
    def ind2(e, L, n):
        if L == []:
            return n
        if L == '':
            return n
        if e == L[0]:
            return n
        return ind2(e, L[1:], n + 1)
    return ind2(e, L, 0)

def removeAll(e, L):
    """Return another list that is identical to L except that all elements identical to e have been removed"""
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def even(X):
    if X % 2 == 0 : return True
    else: return False

def myFilter(func, L):
    """Return a filtered list """
    if L == []:
        return []
    if func(L[0]) == False:
        return myFilter(func, L[1:])
    return [L[0]] + myFilter(func, L[1:])


def deepReverse(L):
    """"Returns the reversal of the list where, additionally, any element that is a list is also deepReversed"""
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[0:len(L)-1])
    return [L[-1]] + deepReverse(L[0:len(L)-1])

