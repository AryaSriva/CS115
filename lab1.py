############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    """returns the reciprocal of number inputted"""
    return 1.0/x


def e(n):
    """returns the approximation of the mathematical value e using a Taylor Series with the first n terms"""
    newList = map(factorial, range(0, n+1))
    taylorList = map(inverse, newList)
    return reduce(add, taylorList)

def add(x, y):
    """returns sum of x and y"""
    return x + y
