class Solution:
    def permute(self, nums) :
        
        def dp(i , arr):
            item = arr.pop(i)
            if len(arr) == 0:
                return [[item]]
            result = None
            for index in range(arr):
                result = dp(index , arr)
                for eachArr in result:
                    eachArr.append(item)
            return result
    
        results =None
        for i1 in range(len(nums)):
            result = dp(i1 , *nums)
            results.append(result)
        return results
    


print(Solution().permute([1,2,3]))