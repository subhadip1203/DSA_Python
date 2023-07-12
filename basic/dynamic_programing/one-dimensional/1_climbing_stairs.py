"""
Leetcode : https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Video : https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=1624s
 
"""

class Solution:
    def climbStairs(self, n):
        
        # current is i postition , next is i+1 position
        current , next = 1, 0

        for i in reversed(range (n)):
            temp = current
            current  = current+next
            next = temp
        
        return current
    
n = 5
print(Solution().climbStairs(n))