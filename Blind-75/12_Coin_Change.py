'''
leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


'''

def calculateNumber(coins, amount, result , currentTotal = 0 , currentCombination = []):
    if currentTotal == amount:
        result.append(currentCombination)
    if currentTotal > amount:
        return

    for x in coins:
        newTotal = currentTotal +  x
        calculateNumber(coins, amount, result, newTotal , [*currentCombination,x])
           



def coinChange(coins, amount):
    result = []
    calculateNumber(coins, amount, result)
    # print(result)
    smallest = len(result[0]) if len(result) > 0 else -1
    for x in result:
        if len(x) < smallest:
            smallest = len(x)
    return smallest

coins = [1,2,5,]
amount = 11
print(coinChange(coins, amount))