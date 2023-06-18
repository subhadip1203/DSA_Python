'''
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''

def maxArea( height ):
    low = 0
    high = len(height) -1
    result = 0
    while low < high :
        currentVolume = (high-low) * min(height[high], height[low])
        result=  max(result,currentVolume)
        if height[high] < height[low] :
            high -=1
        else:
            low += 1
    return result

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

height = [1,1]
print(maxArea(height))