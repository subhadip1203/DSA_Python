# https://www.codingninjas.com/studio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
# https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0pwFf-BnpkXxs0Ra0eU2sJY
# time: 29:20

def dp(arr):
    
    result = [0 for _ in range(len(arr))]

    last_step = float('inf')
    second_last_step = float('inf')
    
    for i in range(1, len(arr)):
        last_step = result[i-1] + abs( arr[i] - arr[i-1])
        if i>1:
            second_last_step = result[i-2] + abs( arr[i] - arr[i-2])
        result[i] = min(last_step , second_last_step) 
    print(result)
    return result[len(arr)-1]


arr = [10, 20, 30, 10]
print(dp(arr))