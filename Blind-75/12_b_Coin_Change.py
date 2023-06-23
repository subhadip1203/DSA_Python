'''
leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


'''

import math

def calculateNumber(coins, remaining , result , current =[]):
    if remaining == 0 and len(result['value']) > len(current):
        result['value'] = current
    if remaining < 0:
        return None
    for x in coins :
        calculateNumber(coins, remaining - x , result, [*current , x])
       





def coinChange(coins, amount):
    result = {
        'value' : [1 for i in range(amount+1)]
    }
    calculateNumber(coins,amount, result)
    return [] if len(result['value']) > amount else result['value']


coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2,1]
amount = 3
print(coinChange(coins, amount))

coins = [1]
amount = 3
print(coinChange(coins, amount))