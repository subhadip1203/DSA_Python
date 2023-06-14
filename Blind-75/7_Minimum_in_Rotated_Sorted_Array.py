'''
Leetcode : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
'''

def findMin( nums) :
    if len(nums) == 0:
        return None
    else:
        low = 0
        high = len(nums)-1
        while low < high -1 :
            mid = (low + high)//2
            if nums[low] < nums[mid]:
                low = mid 
            else:
                high = mid
            print(low, mid,  high)

        # it sthe position where max-number(low index) , min-number (high index)
        # returnning high index or left
        if nums[high] < nums[low]:
            return nums[high]  
        # its a sorted array no rotation , so lowest number is the first one
        else:
            return  nums[0]
    
        
        
            

nums = [3,4,5,1,2]
print(findMin( nums) )

nums = [4,5,6,7,0,1,2]
print(findMin( nums) )

nums = [11,13,15,17]
print(findMin( nums) )

nums = [1]
print(findMin( nums) )

nums =[3,1,2]
print(findMin( nums) )


nums =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print(findMin( nums) )