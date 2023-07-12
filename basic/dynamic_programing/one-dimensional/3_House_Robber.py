"""
Leetcode : https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is 
that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 
video : https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=1624s
video : https://www.youtube.com/watch?v=VXqUQYGMnQg
"""

class Solution:
    def rob(self, nums):
        # for max rob till i index  will be either
        # option 1: rob at i + max rob till (i-2)
        # option 2: max rob till i-1

        for i in range(len(nums)):
            option1 = nums[i] + (nums[i-2] if i >=2 else 0)
            option2 = nums[i-1] if i >=1 else 0
            nums[i] = max(option1 , option2)
        
        return nums[len(nums)-1]



nums = [1,2,3,1]
print(Solution().rob(nums))

nums = [2,7,9,3,1]
print(Solution().rob(nums))

nums = [2,7,3,1,4,2,1,8]
print(Solution().rob(nums))