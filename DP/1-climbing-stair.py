'''

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''


def minCostClimbingStairs(arr):
    
    arr.append(0)
    for i in range(2,len(arr)):
        one_step = arr[i] + arr[i-1]
        two_step = arr[i] + arr[i-2]
        arr[i] = min(one_step,two_step)
    return arr




cost = [10,15,20]
print(minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))