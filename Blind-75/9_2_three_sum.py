'''
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
def arrangeNumber (small , big , unknown) :
    if unknown < small :
        return (unknown , small , big) 
    elif unknown > big :
        return (small , big , unknown)
    else:
        return (small , unknown ,big)

def twoSum (arr , noTouchIndex , targetSum , result):
    start = 0
    end = len(arr) -1
   
    while start < end :
        if start == noTouchIndex:
            start += 1
        elif end == noTouchIndex:
            end -= 1
        else:
            # when additin is equal to targer
            if arr[start] + arr[end] + arr[noTouchIndex]  == targetSum:
                if noTouchIndex == 1  :
                    print(start , end, noTouchIndex , arr[start] , arr[end] , arr[noTouchIndex] )
                result.add(arrangeNumber (arr[start] , arr[end] , arr[noTouchIndex]) )
                start += 1
                end -= 1
            # if addition low , increase start
            elif arr[start] + arr[end] < targetSum:
                start += 1
            # if addition high , decrease end
            else:
                end -= 1


def threeSum(nums ) :
    arr = sorted(nums)
    print(arr)
    result = set()
    target = 0
    for i in range (len(arr)):
        twoSum (arr , i , target , result)
    finalResult = []
    for x in result:
       finalResult.append(list(x))

    return finalResult


# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

# nums = [-1,0,1,0]
# print(threeSum(nums))

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(threeSum(nums))