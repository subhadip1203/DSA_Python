# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# solution youtube : https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3&t=535s

'''
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Hint for :
    1. question will be of Array (or string)
    2. need sub_array or sub_string
    3. given  window size for condition ( fixed size windows ) 
    4. given condition  to get windows size ( variable size windows )

'''


# def getMaxSubArr(Arr,K):  
#     N = len(Arr)
#     l,r = 0,0
#     max_=0
#     sum_=0
#     while r<N:
#         sum_ += Arr[r]
#         if r >= K-1:
#             max_ = max(max_,sum_)
#             sum_ -= Arr[l]
#             l += 1
#         r+=1
#     return max_


def getMaxSubArr(Arr,windowSize):  
    max_index= len(Arr)-1
    
    left,right = 0,1
    maxVal= Arr[left]
    sumVal= Arr[left]
    
    while right-left+1 <= windowSize :
        sumVal += Arr[right]
        maxVal = sumVal
        right += 1
    
    print("step ", left+1 ," : ",sumVal)
   
    
    while right <= max_index:
        sumVal = sumVal + Arr[right] - Arr[left]
        maxVal = max(maxVal,sumVal)
        left,right = left+1 ,right+1
        print("step ", left+1 ," : ",sumVal)

    return maxVal

K = 2
Arr = [20,100, 900, 300, 400]
print(getMaxSubArr(Arr,K))
print("-----")

K = 4
Arr = [50,100, 200, 300, 400]
print(getMaxSubArr(Arr,K))
