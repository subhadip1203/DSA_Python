

def search(arr , item):
    start = 0
    end = len(arr) -1

    while start < end - 1 :
        mid = (start+end)//2
        if arr[mid] < item :
            start = mid
        else:
            end = mid
        
    if arr[start] == item :
        print('start')
        return start
    if arr[end] == item :
        print('end')
        return end



arr = [1,2,3,4,5,6,7,8,9]
item = 2
print(search(arr,item))