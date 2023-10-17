def maxProfitColdown(prices):
        n = len(prices)
        if n == 1: return 0
        b = [-10 ** 9] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i - 1], b[i - 1] + prices[i] )
            b[i] = max(b[i - 1], s[i - 2] - prices[i] )
            
        print(b)
        print(s)
        return s[-1]


def maxProfit(prices):
        n = len(prices)
        if n == 1: return 0
        b = [-10 ** 9] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i - 1],  b[i - 1] + prices[i])
            b[i] = max(b[i - 1],  s[i - 1] - prices[i])
            
        print(b)
        print(s)
        return s[-1]

def maxProfitwithFee(prices,fee):
        n = len(prices)
        if n == 1: return 0
        b = [-10 ** 9] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i - 1],  b[i - 1] + prices[i] -fee)
            b[i] = max(b[i - 1],  s[i - 1] - prices[i])
            
        print(b)
        print(s)
        return s[-1]


prices = [1,2,3,0,2,1,4,0,9]

print(maxProfitColdown(prices))
print(maxProfit(prices))

prices = [1,3,2,8,4,9]
fee = 2
print(maxProfitwithFee(prices , fee))

prices = [1,3,7,5,10,3]
fee = 3
print(maxProfitwithFee(prices , fee))
