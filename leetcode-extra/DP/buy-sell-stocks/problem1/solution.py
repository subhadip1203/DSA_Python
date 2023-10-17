# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Best Time to Buy and Sell Stock


def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        currentProfit = prices[i] - min_price
        max_profit = max(max_profit , currentProfit)
        min_price = min(min_price,prices[i])

    return max_profit

prices = [7,1,5,3,6,4]
