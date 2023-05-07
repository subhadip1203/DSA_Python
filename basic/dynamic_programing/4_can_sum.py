def canSum(num, arr, memo={}) :
    if num in memo: return memo[num]
    if num ==0 : return True
    if num < 0 : return False

    result = False 
    for x in arr:
        subResult = canSum(num-x, arr,memo)
        if subResult == True:
            result = True
    memo[num] = result
    return  result



print(canSum(7000,[23,51,77]))