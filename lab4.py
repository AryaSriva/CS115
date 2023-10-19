############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab4
#  
############################################################
from functools import reduce

def knapsack(capacity, itemList):
    """returns a list of all the items we can take without exceeding our knapsack capacity
    and the total value of those items"""
    if capacity == 0 or itemList == []:
        return [0, []]
    elif itemList[-1][0] > capacity:
        return knapsack(capacity, itemList[:-1])
    else:
        useItem = knapsack(capacity - itemList[-1][0], itemList[:-1])
        loseItem = knapsack(capacity, itemList[:-1])
        useItem[0] += itemList[-1][-1]
        useItem[1] += [itemList[-1]] 
        return max(useItem, loseItem)
