#  https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution:
    def numSubarraysWithSum(self, nums, goal):
        # 2 pointer approach

        # start and end both starts from 0
        start = 0
        end = 0

        # sum = first elemet
        sum = 0


        # result initially 0
        result = 0

        # while start is not going to the last index , keep it up

        while end < len(nums):

            if sum == goal : 
                print('result',result, 'sum', sum, 'end', end)
                result += 1
                end += 1
            
            while sum > goal:
                goal -= nums[start]
                start += 1
        

            while sum < goal:
                sum +=  nums[end]
                end += 1
                print('result',result, 'sum', sum, 'end', end)

        return result



nums = [1,0,1,0,1]
goal = 2
print(Solution().numSubarraysWithSum(nums,goal))