
def maxProfit(prices , K):
    # newArr =[0]
    
    # for i in range(1, len(prices)):

    #     profit = prices[i] - prices[i-1]
    #     if profit >0:
    #         newArr.append(profit)
    #     else:
    #         newArr.append('-')
        
    # print(newArr)

    # for i in range(1, len(newArr)-1):
    #     if newArr[i] != '-' and newArr[i+1] != '-':
    #         newArr[i+1] = newArr[i+1] +newArr[i]
    #         newArr[i] = '0'
    
    # print(newArr)

    profits = []

    tempProfit = 0
    for i in range(1, len(prices)):

        profit = prices[i] - prices[i-1]
        
        if profit >0:
            tempProfit += profit
            print(tempProfit)

            if i == len(prices)-1 and tempProfit > 0:
                profits.append(tempProfit)
            
            if i < len(prices)-1 and prices[i+1] < prices[i]:
              profits.append(tempProfit)
              tempProfit = 0

    print(profits)


prices = [3,3,5,8,0,0,3,1,4]
print(maxProfit(prices , 2))


prices = [1,2,3,4,5]
print(maxProfit(prices , 2))