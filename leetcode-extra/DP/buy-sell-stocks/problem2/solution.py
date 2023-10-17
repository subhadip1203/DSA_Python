# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


def maxProfit(prices):
    arr_len = len(prices)
    
    # create extra space array 2 row array
    # row 1 is buy
    # row 2 is sell
    hold = [ 0 for _ in range(arr_len)]
    hold[0] = prices[0]
    
    not_hold = [ 0 for _ in range(arr_len)]
    
    
    for i in range(1,arr_len):
        
        #  for holding
        #  hold[index]  = max( keep you stock, or  latest not-holding status - buy stock today price )
        hold[i] = max( hold[i-1] , not_hold[i-1] - prices[i] )
      

        #  for not holding
        #  not_hold[index]  = = max(keep your stock , or latest holding status - sell the stock today price)
        not_hold[i] = max( not_hold[i-1]  , hold[i-1]+ prices[i] )
       


    print(hold , not_hold)



prices = [7,1,5,3,6,4]
maxProfit(prices)
