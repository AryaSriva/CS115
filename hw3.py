'''
Created on 10/6/22
@author:   Aryaman Srivastava
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    """returns the minimum number of coins and which coins to use to get a given amount"""
    if amount <= 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        useIt = giveChange(amount - coins[0], coins)
        loseIt = giveChange(amount, coins[1:])
        useIt[0] += 1
        useIt[1] += [coins[0]]
        return min(useIt, loseIt)

# your code goes here                
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    """return list with words in dct and their scores"""
    if dct == []:
        return []
    else:
        func = lambda x: [x] + [getWordScore(x, scores)]
        return list(map(func, dct))
def getLetterScore(letter, scores):
    """get score for a given letter"""
    if scores == []:
        return 0
    elif letter == scores[0][0]:
        return scores[0][1]
    else:
        return getLetterScore(letter, scores[1:])

def getWordScore(word, scores):
    """get score for a word by adding up scores for each letter in the word"""
    if word == "":
        return 0
    else:
        return getLetterScore(word[0], scores) + getWordScore(word[1:], scores)




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    """returns a list with elements with indices in the range [0, n) from the original list"""
    if L == [] or n == 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    """returns a list with elements with indices in the range [n, length of list) from the original list"""
    if L == []:
        return []
    elif n == 0:
        return L
    else:
        return drop(n-1, L[1:]) 
