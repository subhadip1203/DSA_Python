# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


def maxProfit(prices):
    arr_len = len(prices)

    no_stock_in_hand = [0 for _ in range(arr_len)]
    stock_in_hand = [0 for _ in range(arr_len)]
    sold_all_stock = [0 for _ in range(arr_len)]

    # on the first day , we only can buy stock.
    # on stock in hand  = 0
    # can not sell , so sold_all_stock = 0
    # negative means we bought stock
    stock_in_hand[0] = - prices[0]

    for i in range(1,arr_len):
        # for today no stock in hand means :
        # Last day we also had no stock in hand
        # or 
        # previous day we sold stock
        no_stock_in_hand[i]  =  max( no_stock_in_hand[i-1] , sold_all_stock[i-1] )


        # for today if we have stock in hand  means :
        #  previous day we had stock in hand
        # or
        # previous day we had no stock + we are buying stock today 
        # ( lastday no_stock_in_hand - today stock price )
        stock_in_hand[i] = max(stock_in_hand[i-1], no_stock_in_hand[i-1] - prices[i] )



        # for today if we selling stock , means
        # previous day we had some stock in hand +  today stock
        sold_all_stock[i] = stock_in_hand[i-1] + prices[i]


    return max ( no_stock_in_hand[arr_len-1] , sold_all_stock[arr_len-1])

prices = [1,2,3,0,2]