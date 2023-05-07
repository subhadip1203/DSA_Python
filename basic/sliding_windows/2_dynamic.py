# dynamic sliding windows

def sum(arr , num):
    minimumLength = len(arr)
    if minimumLength == 0 :
        return 0
    
    start = 0
    end = 0
    currentSum = 0
    while end < len(arr):
        currentSum = currentSum +arr[end]
        end = end+1

        while start < end and currentSum >= num:
            currentSum = currentSum -arr[start]
            start = start+1

            minimumLength = min(minimumLength , end-start+1)
    
    return(minimumLength)

print(sum([1,2,3,4,5,6],7))