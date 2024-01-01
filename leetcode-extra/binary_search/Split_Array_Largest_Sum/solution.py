# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/description/


class Solution:
    def splitArray(self, nums, k):

        def can_split_within_k (nums , k , midVal):
            currentSum = 0
            num_of_split = 1
            for item in nums:
                if currentSum + item > midVal:
                    currentSum = 0
                    num_of_split += 1
                currentSum += item

            return True if num_of_split<= k else False


        maxArrItem = 0
        sumArray = 0
        for val in nums:
            maxArrItem = max(maxArrItem , val)
            sumArray += val

        start = maxArrItem
        end = sumArray

        while start < end:
            midValue = (start+end)//2

            # if true , means midvalue should increase
            if can_split_within_k (nums , k , midValue):
                end = midValue
            else:
                start = midValue+1

        return end





nums = [7,2,5,10,8]
k = 2
print( Solution().splitArray(nums, k))


nums = [1,2,3,4,5]
k = 2
print( Solution().splitArray(nums, k))
