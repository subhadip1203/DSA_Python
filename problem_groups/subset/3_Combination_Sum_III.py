'''
leetcode : https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.

'''

def calculateCombinationSum(arr, resultLen, targetSum , result, index=0 , current=[] , currentSum=0):
    if currentSum == targetSum and len(current) == resultLen:
        result.append(current.copy())
    for i in range(index, len(arr)):
        # current.append(arr[i])
        # currentSum = currentSum+arr[i]
        calculateCombinationSum(arr, resultLen, targetSum , result, i+1 , [*current, arr[i]], currentSum+arr[i])
        # current.pop()
        # currentSum = currentSum-arr[i]



def combinationSum3(k,n):
    arr = [1,2,3,4,5,6,7,8,9]
    result = []
    calculateCombinationSum(arr,k, n, result)
    return result

k = 3
n = 7
print(combinationSum3(k,n))

k = 3
n = 9
print(combinationSum3(k,n))