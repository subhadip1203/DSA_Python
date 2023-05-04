
def binarySearch(arr, item ):
    start = 0
    end = len(arr)
    while start <= end :
        mid = (end+start)//2
        print(start , mid, end)
        if arr[mid] == item:
            return mid
        elif arr[mid] < item :
            start = mid+1
        else :
            end = mid-1
       
    return -1


myArr = [1,3,6,9,12,21,54,78,90]
searchItem = 11

print(binarySearch(myArr,searchItem))