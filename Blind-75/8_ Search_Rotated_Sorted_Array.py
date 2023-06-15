'''
leetcode : https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

def bunarySeaech(nums ,newLow , newHigh , target) :
    # Basic binary search
    if nums[newLow] == target:
        return newLow
    if nums[newHigh] == target:
        return newHigh
    while newLow < newHigh -1 :
        mid = (newLow+newHigh) // 2
        if nums[mid] == target:
            return mid
        elif target <  nums[mid] : 
            newHigh = mid
        else: 
            newLow = mid
    return -1


def search( nums, target):
    # first search the pivot point
    low = 0
    high = len(nums) -1

    while low < high -1 :
        mid = (low+high)//2
        if nums[low] < nums[mid]:
            low = mid
        else:
            high = mid
    
    pivot = 0
    if nums[high] < nums[low]:
        pivot = high
    
    # select the left or right part of pivot , where to find teh number
    newLow = 0
    newHigh = len(nums) -1
    
    if nums[pivot] <=  target and target <= nums[newHigh]:
        newLow = pivot
    elif nums[newLow] <=  target and target <= nums[pivot-1]:
        newHigh = pivot-1
    
    return bunarySeaech(nums , newLow , newHigh ,  target) 



     
        
    



# nums = [4,5,6,7,0,1,2]
# target = 0
# print(search( nums, target))

# nums = [4,5,6,7,0,1,2]
# target = 3
# print(search( nums, target))

# nums = [2]
# target = 2
# print(search( nums, target))

# nums = [2]
# target = 0
# print(search( nums, target))

nums = [4,5,6,7,0,1,2]
target = 1
print(search( nums, target))