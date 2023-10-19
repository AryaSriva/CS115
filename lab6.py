'''
Created on 10/19/22
@author:   Aryaman Srivastava
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 != 0

    """base-2 representation of 42: 101010"""
    
    """If the base-10 number is odd, the rightmost bit will be 1 and
    if the number is even, the rightmost bit will be 0 because
    in a base-2 representation, the rightmost bit represents the number 1.
    Since all other bits in a base-2 representation are even, the only way
    to get an odd number is to have the rightmost bit be 1 and if the number
    is even, there is no need for the value of 1, so the rightmost bit would
    be 0."""
    
    """The number is getting divided by the base, in this case 2."""
    
    """In the case that N is odd, we would add a 1 at the end of the base-2
    representation of N/2. If N is even, we would add a 0 at the end of the
    base-2 representation of N/2"""

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int(s[-1]) == 0:
        return 2*binaryToNum(s[:-1]) 
    else:
        return 2*binaryToNum(s[:-1]) + 1

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if '0' not in s:
        return len(s)*'0'
    else:
        return (len(s) - len(numToBinary(binaryToNum(s) + 1)))*'0' + numToBinary(binaryToNum(s) + 1)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        print(s)
        return count(increment(s), n-1)


"""The ternary representation for 59 is 2012 as you can write 59 as
    2*27 + 0*9 + 1*3 + 2*1 = 59"""    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n%3 == 1:
        return numToTernary(n//3) + '1'
    elif n%3 == 2:
        return numToTernary(n//3) + '2'
    else:
        return numToTernary(n//3) + '0'
        
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int(s[-1]) == 1:
        return 3*ternaryToNum(s[:-1]) + 1
    elif int(s[-1]) == 2:
        return 3*ternaryToNum(s[:-1]) + 2
    else:
        return 3*ternaryToNum(s[:-1])

