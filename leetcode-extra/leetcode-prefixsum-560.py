#  video : https://www.youtube.com/watch?v=fFVZt-6sgyo&t=13s

class Solution:
    def subarraySum(self, nums, k):
        
        # result 
        result = 0

        # prefix sum table
        prefix_sum_table = {}
        #adding for 0 . 0 has 1 occurance
        prefix_sum_table[0] = 1

        # default sum = 0 
        currentSum = 0



        for x in nums:
            currentSum += x
           

            # cheking if currentsum - target value is in the prefix table
            key = currentSum - k
            if key in prefix_sum_table:
                result += prefix_sum_table[key]
            
            # adding current sum to prefix table
            prefix_sum_table[currentSum] = prefix_sum_table.get(currentSum , 0)+1
        
        return result