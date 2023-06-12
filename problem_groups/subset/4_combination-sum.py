'''
Leetcode : https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.
'''

def getCombinations(arr, targetSum, resultArr , index = 0 , currentArr = [] , currentSum = 0 ):

    if currentSum == targetSum:
        resultArr.append(currentArr)
    elif currentSum > targetSum:
        return
    else:
        for i in range(index, len(arr)):
            getCombinations(arr, targetSum, resultArr , i ,  [*currentArr, arr[i]] , currentSum+arr[i] )
    


def combinationSum(candidates, target):
    result = []
    getCombinations(candidates, target,result)
    return result


candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))