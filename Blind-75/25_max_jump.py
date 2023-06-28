'''
Leetcode : https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''

def canJump( nums):
    targetIndex = len(nums)-1
    startIndex = targetIndex-1

    while startIndex >= 0 :
        if targetIndex - startIndex <= nums[startIndex] :
            targetIndex = startIndex
        
        startIndex -= 1

    return True if( targetIndex == 0) else False
       

nums = [2,3,1,1,4]
print( canJump(nums) )


nums = [3,2,1,0,4]
print( canJump(nums) )


nums = [0,1]
print( canJump(nums) )