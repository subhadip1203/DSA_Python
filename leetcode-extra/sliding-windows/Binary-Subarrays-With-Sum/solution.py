# https://leetcode.com/problems/binary-subarrays-with-sum/description/


class Solution:
    def numSubarraysWithSum(self, nums, goal):

        # result =0
        result = 0


        # both start and end is zero
        start = end = 0

        # sum initially zero
        sum = 0

        

        while end < len(nums):
            sum += nums[end]
            end += 1
            

            if sum == goal:
                result += 1
            
            if sum > goal :
                while start < end and sum >= goal:
                    sum -= nums[start]
                    start += 1

                    if sum == goal:
                        result += 1


        
        return result


nums = [1,0,1,0,1]
goal = 2
print(Solution().numSubarraysWithSum(nums, goal))

nums = [0,0,0,0,0]
goal = 0
print(Solution().numSubarraysWithSum(nums, goal))