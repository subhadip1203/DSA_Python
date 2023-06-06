'''
leetcode : https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible  subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
'''



def calculateSubSet(arr,result, index=0 , current=[]):
    result.append(current)
    for i in range(index, len(arr)):
        if  i > index and arr[i-1] == arr[i] : 
            continue
        else:
            calculateSubSet(arr, result, i+1 , [*current, arr[i]])
        



def subsetsWithDup(nums):
    result = []
    calculateSubSet(sorted(nums),result)
    return result


# def subsetsWithDup(nums):
#     def dfs(start, path, res):
#         res.append(path)
#         for i in range(start, len(nums)):
#             if i > start and nums[i] == nums[i-1]:
#                 continue
#             dfs(i+1, path + [nums[i]], res)
        
#     nums.sort()
#     res = []
#     dfs(0, [], res)
#     return res

nums = [1,2,2]
print(subsetsWithDup(nums))

nums = [4,4,4,1,4]
print(subsetsWithDup(nums))