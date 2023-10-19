def countOddEntries(L):
    """
    Function accepts a list of integer numbers.
    Iterates through the list with a "while" loop and counts the odd numbers.
    Returns the count of odd numbers.
    """
    count = 0
    while (len(L) > 0):
        if L[0] % 2 != 0:
            count += 1
        L = L[1:]
    return count

def testOddEntries():
    assert countOddEntries([1, 3, 4, 5, 6]) == 3
    assert countOddEntries([]) == 0
    assert countOddEntries([2, 4, 6]) == 0
    assert countOddEntries([1, 3, 5, 7, 9]) == 5

testOddEntries()
