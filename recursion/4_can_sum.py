
def canSum(num, arr) :
    if num ==0 : return True
    if num < 0 : return False
    result = False 
    for x in arr:
        subResult = canSum(num-x, arr)
        if subResult == True:
            result = True
    return  result



print(canSum(7000,[23,51,77]))