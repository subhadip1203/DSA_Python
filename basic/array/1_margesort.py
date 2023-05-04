
def margeSortedArr(left,right):
    left_index = right_index = 0
    newArr = []

    while left_index < len(left) and right_index < len(right) :
        if left[left_index] <= right[right_index]:
            newArr.append(left[left_index])
            left_index = left_index+1
        else:
            newArr.append(right[right_index])
            right_index = right_index+1

    while left_index < len(left):
        newArr.append(left[left_index])
        left_index = left_index+1
    
    while right_index < len(right) :
        newArr.append(right[right_index])
        right_index = right_index+1

    return newArr


def margesort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid_point = len(arr)//2
        left_part = arr[0:mid_point]
        right_part = arr[mid_point:len(arr)]
        
        left_sorted_arr = margesort(left_part)
        right_sorted_arr = margesort(right_part)
        
        marged_arr = margeSortedArr(left_sorted_arr,right_sorted_arr)
        return marged_arr


myArr = [1,6,30,9,2,3,4,1,169,12,30,1,7]
print(margesort(myArr))