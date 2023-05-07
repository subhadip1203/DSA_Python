
def slidingWindow(arr, num):
    addUp =0
    result = []
    for x in range( num ):
        addUp += arr[x]
    result.append(addUp)

    for x in range(num, len(arr)):
        addUp = addUp - arr[x-3] + arr[x]
        result.append(addUp)
    
    print(result)

arr = [1,2,3,4,5,6,7,8,9]
slidingWindow(arr, 3)