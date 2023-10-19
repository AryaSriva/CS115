############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 HW1
#  
############################################################
from functools import reduce

def factorial(n):
    """returns the factorial of given number n"""
    return reduce(multiply, range(1, n+1))

def multiply(x, y):
    """returns product of x and y"""
    return x*y

def mean(L):
    """returns mean of numbers in list L"""
    sum = reduce(add, L)
    return sum/len(L)

def add(x, y):
    """returns sum of x and y"""
    return x + y 


