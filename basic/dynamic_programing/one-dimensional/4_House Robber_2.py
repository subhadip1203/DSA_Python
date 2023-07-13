"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # rob house individual array
        def robOneArr(arr):
            # option 1: value of i + max value of i-2
            # option 2: max value of i-1
            
            for i in range (len(arr)):
                option1 = arr[i] + (arr[i-2] if i>=2  else 0)
                option2 = arr[i-1] if i>=1 else 0
                arr[i] = max(option1,option2)
            
            return arr[len(arr)-1]
        
        # start array will not keep the last  item of nums
        # end   array will not keep the first item of nums
        startArr = []
        endArr = []
        for i in range(len(nums)-1):
           startArr.append(nums[i]) 
           endArr.append(nums[i+1]) 

        result = max(robOneArr(startArr) , robOneArr(endArr))
        return result

nums = [2,3,2]
print(Solution().rob(nums))

nums = [1,2,3,1]
print(Solution().rob(nums))

nums = [0]
print(Solution().rob(nums))