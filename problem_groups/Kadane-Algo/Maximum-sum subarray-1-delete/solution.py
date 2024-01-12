'''
    https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
'''

class Solution:
    def maximumSum(self, arr):
        maxval = arr[0]
        leftArr = [0 for _ in range(len(arr))]

        for i in range(len(arr)):
            leftArr[i] = max( arr[i] , leftArr[i-1]+arr[i] if i-1>=0 else arr[i] )
            maxval = max(maxval , leftArr[i])

        rightArr = [0 for _ in range(len(arr))]
        for i in reversed(range(len(arr))):
            rightArr[i] = max( arr[i] , rightArr[i+1]+arr[i] if i+1<len(arr) else arr[i] )
            maxval = max(maxval , rightArr[i])

        print(leftArr)
        print(rightArr)

        result = maxval
        for i in range(1, len(arr)-1 ):
            result = max( result, leftArr[i-1]+rightArr[i+1] )
        
        return result


arr = [1,-2,0,3]
print(Solution().maximumSum(arr))

arr = [1,-2,-2,3]
print(Solution().maximumSum(arr))

arr = [-1,-1,-1,-1]
print(Solution().maximumSum(arr))
        