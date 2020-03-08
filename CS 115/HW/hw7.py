'''
Created on 10/23/19
@author:   Jonathan Joshua
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS 115 - hw7
'''

FullAdder = { ('0','0','0') : ('0','0'),('0','0','1') : ('1','0'),('0','1','0') : ('1','0'),('0','1','1') : ('0','1'),('1','0','0') : ('1','0'),('1','0','1') : ('0','1'),('1','1','0') : ('0','1'),('1','1','1') : ('1','1') }

def numToBaseB(N,B):
    """Takes as input a non-negative (0 or larger)integer N and a base B (between 2 and 10 inclusive) and returns a string representing the number N inbase B."""
    if N == 0: return "0"
    def numBase(N,B):
        if N == 0: return ""
        return numBase(N//B,B) + str(N%B)
    return numBase(N,B)


def baseBToNum(S, B):
    '''Returns an integer in base 10 representing the same number as S.'''
    if S == '':
        return 0
    return B * baseBToNum(S[0:-1], B) + int(S[-1])

def baseToBase(B1, B2, SinB1):
    '''Returns a string representing the same number in base B2.'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    """Takestwo binary strings S and T as input and returns their sum."""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB(S,T):
    """Returns a new string representing the sum of the two input strings."""
    def helper(S,T,carry):
        if S == '' and T == '' and carry == '1':
            return '1'
        if S == '' and T == '' and carry == '0':
            return ''
        elif T == '':
            sum = FullAdder[(S[-1],'0',carry)]
        elif S == '':
            sum = FullAdder[('0',T[-1],carry)]
        else:
            sum = FullAdder[(S[-1],T[-1],carry)]
        return helper(S[:-1],T[:-1],sum[1]) + sum[0]
    return helper(S,T,'0')
