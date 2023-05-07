def howSum(arr,num, memo=None):
    if memo == None: memo = {}
    
    if memo.get(num) : return memo[num]
    elif num == 0 : return []
    elif num < 0 : return None
    else:
        for x in arr:
            reminder = num-x
            reminderResult = howSum(arr,reminder,memo)
            if reminderResult != None:
                returnResult = [x,*reminderResult]
                memo[x] = returnResult
                return memo[x]

    memo[num] = None
    return None



print(  howSum([2,3],7)  )
print(  howSum([7,13],100)  )