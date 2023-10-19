'''
Created on 26th September 2022
@author:   Aryaman Srivastava
Pledge:    I pledge my honor that I abided by the Stevens Honor System
CS115 - Hw 2
'''
import sys
from functools import reduce
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scoreList):
    """returns score for a given letter based on scores in scoreList"""
    if scoreList[0][0] == letter:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    """returns scrabble score for given word S"""
    if S == "":
        return 0
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def scoreList(Rack):
    """returns a list of all words in Dictionary that can be made from letters in Rack and scores for each one"""
    if Rack == []:
        return ['', 0]
    else:
        func = lambda x: x == checkLettersInWord(Rack, x)
        newList = list(filter(func, Dictionary))
        return append(newList)
    
def bestWord(Rack):
    """returns the highest scoring word that can be made from the letters in Rack"""
    if Rack == []:
        return ['', 0]
    else:
        return findHighestScore(scoreList(Rack))
            
def findHighestScore(lst):
    """returns highest scoring word in a given list of words with their respective scores attached.
        First acquires the score for the first word and then filters the entire list for words with a score higher than that of the first word.
        Then runs the new list through the function again and each consecutive new list again until only one element in the list remains, the word with the highest score"""
    if lst == []:
        return ['', 0]
    elif len(lst) == 1:
        return lst[0]
    else:
        scoreMin = lst[0][1]
        func = lambda x: x[1] > scoreMin
        newList = list(filter(func, lst))
        return findHighestScore(newList)
    
def checkLettersInWord(Rack, word):
    """checks if letters in rack can make the word given"""
    if word == "":
        return ""
    elif word[0] in Rack:
        return word[0] + checkLettersInWord(removeLetters(Rack,word[0]), word[1:])
    else:
        return checkLettersInWord(Rack, word[1:])

def removeLetters(Rack, letter):
    """removes letters already used in the word in rack"""
    if Rack == []:
        return []
    elif Rack[0] == letter:
        return Rack[1:]
    else:
        return [Rack[0]] + removeLetters(Rack[1:], letter)

def append(words):
    """append score for words to the words"""
    if words == []:
        return []
    else:
        return [[words[0]] + [wordScore(words[0], scrabbleScores)]] + append(words[1:])

 
    


