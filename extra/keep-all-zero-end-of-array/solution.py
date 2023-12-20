#  https://www.youtube.com/shorts/uv8tFS2VFuA

def moveZero(arr):
    left = 0
    right = 0

    while right < len(arr):
        if arr[right] != 0:
            print(arr)
            arr[right] , arr[left]  = arr[left] ,  arr[right]
            left += 1
            print(arr)
            print('')
            
        right += 1

    print('----------------------')
    return arr


arr = [1,0,3,0,0,5,7,0,8]
print(moveZero(arr))
