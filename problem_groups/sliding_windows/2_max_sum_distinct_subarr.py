'''
leetcode : https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

You are given an integer array nums and an integer k. 
Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

def maximumSubarraySum(nums, k):
    answer = 0
    currentSum = 0
    arrLen = len(nums)
    dictVal = {}
    
    #=======================================================================
    #       first k items
    #========================================================================

    for i in range(k):
        item = nums[i]
        dictVal[item] = 1 if (item not in dictVal) else dictVal[item]+1
        currentSum = currentSum+ item
    
    if len(dictVal) == k :
        answer = currentSum

    #=======================================================================
    #       after first k items
    #========================================================================
    start = 0
    end = k
    while end < arrLen :
        itemStart = nums[start]
        currentSum = currentSum - itemStart 
        dictVal[itemStart] = dictVal[itemStart] -1
        if dictVal[itemStart]  == 0:
            del dictVal[itemStart]
       

        itemEnd = nums[end]
        currentSum = currentSum+ itemEnd
        dictVal[itemEnd] = 1 if (itemEnd not in dictVal) else dictVal[itemEnd]+1

        if len(dictVal) == k  and answer < currentSum:
            answer = currentSum
        
        start = start+1
        end = end+1
    
    return answer



nums = [1,5,4,2,9,9,9]
k = 3
print(maximumSubarraySum(nums, k))

nums = [9,9,9,1,2,3]
k = 3
print(maximumSubarraySum(nums, k))
