############################################################
# Name: Aryaman Srivastava
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab3
#  
############################################################

def change (amount, coins):
    """returns the least number of coins needed to get given amount from the given list of possible coins"""
    if amount <= 0:
        return 0
    if coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use_coin = 1 + change(amount - coins[0], coins)
        lose_coin = change(amount, coins[1:])
        return min(use_coin, lose_coin)
    
