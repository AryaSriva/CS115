############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 2
#  
############################################################

def dot(L, K):
    """returns the dot product between List/vector L and K"""
    if L == []:
        return 0.0
    elif K == []:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])

def explode(S):
    """returns characters of string S in a list"""
    if S == "":
        return []
    else:
        return list(S[0] + S[1:])

def ind(e, L):
    """returns first index at which element e is found in list L"""
    if L == []:
        return 0
    if L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    """removes all instances of e in list L and returns a new list"""
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def myFilter(func, lst):
    """returns a new list with elements for which function given returns true"""
    if lst == []:
        return []
    elif func(lst[0]) == False:
        return myFilter(func, lst[1:])
    else:
        return [lst[0]] + myFilter(func, lst[1:])

def deepReverse(L):
    """reverses a list as well as elements within the list"""
    if L == []:
        return L
    if isinstance(L[0], list):
        x = L[0]
        return deepReverse(L[1:]) + [deepReverse(x[1:]) + [x[0]]] 
    else:
        return deepReverse(L[1:]) + [L[0]]
