'''
leetcode : https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set). 
The solution set must not contain duplicate subsets. Return the solution in any order.
'''
def generateSubsets(numList , result , index = 0 , currentArr = []):
    result.append(currentArr.copy())
    for i in range(index , len(numList)):
        currentArr.append(numList[i])
        generateSubsets(numList , result , i+1 , currentArr)
        currentArr.pop()


def subsets(nums):
    result = []
    generateSubsets(nums, result)
    return result

nums = [1,2,3]
print(subsets(nums))