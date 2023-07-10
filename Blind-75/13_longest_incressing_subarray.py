'''
Leetcode : https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing 
subsequence
'''



def lengthOfLIS(nums , index = 0 , result = [], current=[]):

    #with out next element
    if nums[index+1] and nums[index] < nums[index+1]:
        lengthOfLIS(nums , index+1, [*current, nums[index] ])

    lengthOfLIS(nums , index+1, current)
        




nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))