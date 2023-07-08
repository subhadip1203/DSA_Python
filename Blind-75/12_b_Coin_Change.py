'''
leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


'''



def coinChange(coins, amount , memo = None):
    if memo == None : memo = {}
    
    if amount == 0:
        return []
    elif amount < 0:
        return None
    elif amount in memo:
        return memo[amount]
    else:
        shortest = None
        for x in coins :
            combinations = coinChange(coins, amount-x , memo)
            if combinations != None:
                newcobination = [*combinations,x]
                if shortest == None or  len(shortest) > len(newcobination):
                    shortest = newcobination
        
        memo[amount] = shortest
        return shortest



coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1,2,5,6]
amount = 30
print(coinChange(coins, amount))