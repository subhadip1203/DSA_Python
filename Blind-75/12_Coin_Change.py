'''
leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


'''

import math

def calculateNumber(coins, rem , cache):

    if rem == 0:
        return 0
    if rem < 0:
        return None
    if rem in cache:
        return cache[rem]
    
    temp = math.inf
    for x in coins :
        newRemain = rem -x
        result = calculateNumber(coins, newRemain, cache )
        if result != None :
            temp = min(temp , result+1)
    cache[rem] = temp
    return cache[rem]


def coinChange(coins, amount):
    ans = calculateNumber(coins,amount, {})
    return -1 if ans ==  math.inf  else ans  


coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))