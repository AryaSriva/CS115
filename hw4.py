'''
Created on 10/13/22
@author:   Aryaman Srivastava
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - HW4
'''

def pascal_row(n):
    """returns a list of elements found in the nth row of Pascal's Triangle"""
    if n <= 0:
        return [1]
    else:
        return [1] + sum_adjacent(pascal_row(n-1)) + [1]


def sum_adjacent(L):
    """sums up adjacent terms from the given list and returns a new list
    with these sums"""
    if L == []:
        return []
    elif len(L) == 1:
        return []
    else:
        return [L[0] + L[1]] + sum_adjacent(L[1:])


def pascal_triangle(n):
    """returns a list of lists with each element containing a row of Pascal's Triangle
    upto and including row n"""
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    """tests if pascal_row function's output matches expected output for a given input"""
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]


def test_pascal_triangle():
    """tests if pascal_triangle function's output matches expected output for a given input"""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1,1], [1,2,1]]
    assert pascal_triangle(3) == [[1], [1,1,], [1,2,1], [1,3,3,1]]

print(pascal_row(1000))
