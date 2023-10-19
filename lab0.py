############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

def same(word):
    '''tells you if the first and last letter of a given word are the same'''
    lowerCaseWord = word.lower()
    lastLetterIndex = len(lowerCaseWord) - 1
    firstLetterIndex = 0
    if (lowerCaseWord[lastLetterIndex] == lowerCaseWord[firstLetterIndex]):
        return True
    else:
        return False
def consecutiveSum(x, y):
    '''returns the sum of consecutive integers between two numbers'''
    num1 = (x+y)/2
    num2 = y - x - 1
    return num1*num2


