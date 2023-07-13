"""
Leetcode : https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

class Solution:
    def coinChange(self, coins, amount):
        maxNumber = amount+1  
        min_coins = [maxNumber for _ in range(amount+1)]
        min_coins[0] = 0 # to make 0 amount we need 0 coin
        
        for i in range(1,len(min_coins)) :
            for coin in coins:
                if coin <= i:
                    min_coins[i] = min(min_coins[i], 1+ min_coins[i-coin])
        
        return min_coins[amount]

coins = [1,2,5]
amount = 11

print(Solution().coinChange(coins,amount))