'''
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

** contiguous subarray
'''


'''
youtube : https://www.youtube.com/watch?v=Y6B-7ZctiW8
'''

def maxProduct( nums ):
    if len(nums) == 0:
        return 0
    else:
        leftProduct = nums[0]
        rightProduct = nums[len(nums)-1]
        result = max(leftProduct, rightProduct)
        i =1
        while i < len(nums):
            leftIndex = i
            rightIndex = len(nums) - (1+i)

            # if old value of leftProduct or rightProduct  is 0 , change them to 1
            leftProduct = 1 if leftProduct == 0 else leftProduct
            rightProduct = 1 if rightProduct == 0  else rightProduct
            
            leftProduct *= nums[leftIndex]
            rightProduct *= nums[rightIndex]

             
            result = max(result ,leftProduct , rightProduct)
            i+= 1

        return result

nums = [2,3,-2,4]
print(maxProduct(nums))

nums = [0,2]
print(maxProduct(nums))

nums = [-3,0,2,-2]
print(maxProduct(nums))

nums = [-2,0,-1]
print(maxProduct(nums))