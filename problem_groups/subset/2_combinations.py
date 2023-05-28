def calculateCombination(arr, result, size, index=0 , current=[]):
    if len(current) == size:
        result.append(current.copy())
    else:
        for i in range(index,len(arr)):
            current.append(arr[i])
            calculateCombination(arr, result, size, i+1 , current)
            current.pop()
    


def combine(n, k):
    result = []
    arr =  [element for element in range(1,n+1)]
    calculateCombination(arr,result , k)
    return result


n = 4
k = 2
print(combine( n,k))