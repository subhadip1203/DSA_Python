"""
Leetcode : https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is 
the cost of ith step on a staircase. Once you pay the cost, 
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

"""

# from i th step to i th step  (i => i): need 1 step
# from i-1 th step to i th step  (i-1 => i): need 1 step

class Solution:
    def minCostClimbingStairs(self, cost):
        #  Add extra elememt to teh end of the cost array
        cost.append(0) 

        # loop from end of array
        for i in reversed(range(len(cost)-2)):
            # check which item has minimum cost
            # ( cost of i + cost i+1 ) or  ( cost of i + cost i+2 ) 
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return (cost[0] if cost[0] < cost[1] else cost[1])




cost = [10,15,20]
print( Solution().minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print( Solution().minCostClimbingStairs(cost))