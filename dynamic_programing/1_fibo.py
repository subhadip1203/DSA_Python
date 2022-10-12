'''
Dynamic Programming is mainly an optimization over plain recursion
'''

def fibo(n , memo ={}):
    if memo.get(n,None) != None :
       return memo[n]

    if n<2:
        return n

    memo[n]=(fibo(n-1,memo)+fibo(n-2,memo))
    return memo[n]

print(fibo(100))