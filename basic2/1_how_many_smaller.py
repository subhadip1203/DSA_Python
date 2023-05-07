
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums) :
    sortedArr = sorted(nums, reverse=True)
    itemDict = {}
    length = len(sortedArr)
    for i in range (length-1) :
        if sortedArr[i] > sortedArr[i+1] :
            itemDict[sortedArr[i]] = length -(i + 1) 
    itemDict[sortedArr[length-1]] = 0

    for i in range(length):
        nums[i] = itemDict[nums[i]]
    
    return nums

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))