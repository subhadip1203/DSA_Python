'''
leetcode :  https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

'''

def maxSubArray(nums):
    i = 1
    maxSum = currentSum = nums[0]

    while i < len(nums):
        
        
        # if nums[i] + currentSum < nums[i]:
        #     currentSum = nums[i]
        # else:
        #     currentSum = currentSum+nums[i]

        # if previousMaxSum + currentVal < currentVal
        # then remove all previousMaxVal 
        # and make previousMaxVal = currentval
        
        currentSum =  max( currentSum + nums[i] ,  nums[i])

        maxSum = max(maxSum , currentSum)
        i+= 1
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

nums = [-6,-10,-3,-4,-12,-2,-1,-5,-4]
print(maxSubArray(nums))

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

nums = [1,2]
print(maxSubArray(nums))