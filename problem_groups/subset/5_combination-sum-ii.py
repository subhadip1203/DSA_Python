'''
leetcode : https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

def calculateCombinations(arr , sumVal , returnArr , index=0 , current=[], currentSum=0):
    if currentSum == sumVal:
        returnArr.append(current)
    elif currentSum > sumVal:
        return
    for i in range(index,len(arr)):
        if i > index  and arr[i-1] == arr[i]:
            continue
        else:
            calculateCombinations(arr , sumVal , returnArr , i+1 , [*current,arr[i]], currentSum+arr[i])

def combinationSum2(candidates, target):
    result = []
    candidates = sorted(candidates)
    print(candidates)
    calculateCombinations(candidates,target ,result )
    return(result)
    

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))