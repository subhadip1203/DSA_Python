'''
leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


'''

def calculateNumber(coins,rem, cache):
    if rem < 0:
        return None
    if rem == 0:                    
        return 0       
    if rem in cache:
        return cache[rem] \
    
    temp = 999999
    for x in coins :     
        result = calculateNumber(coins,rem-x, cache)
        if result != None:
            temp = min(result+1, temp)
    cache[rem] = temp                     
    return cache[rem]
           



def coinChange(coins, amount):
    ans = calculateNumber(coins,amount, {})
    return -1 if ans == 999999 else ans  


coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))