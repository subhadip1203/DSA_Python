'''
leetcode : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''

def maxProfit(prices):
    buy = 0
    sell = 0
    profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            temp_profit = prices[sell] - prices[buy]
            profit = max(profit , temp_profit)
        else:
            buy = sell
        
        sell +=1
    return profit

 
prices = [7,2,5,3,6,1,2]
print(maxProfit(prices))
