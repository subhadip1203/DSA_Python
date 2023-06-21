'''
Leetcode : https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


'''


def climbStairs(n , memo =None):
    # only for first step
    if memo == None : memo = {}
    
    if n == 0 : return 1
    elif n < 0 : return 0
    else: 
        if memo.get(n, None) != None :
            return memo[n]
        else:
            count = climbStairs(n-2 , memo) +climbStairs(n-1, memo)
            memo[n] = count
            return count


n = 43
print(climbStairs(n))