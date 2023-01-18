
def bestSum (num, arr,   memo = None):
    if memo == None : memo = {}

    if memo.get(num) : return memo[num]
    elif num == 0 : return []
    elif num < 0  : return None

    result = None

    for x in arr:
        reminder = num-x
        reminderArr = bestSum (reminder, arr,memo)
        if reminderArr != None:
            newArr = [x, *reminderArr]
            if result == None or   len(newArr) < len(result) :
                result = newArr

    memo[num] = result
    return result

print(bestSum(11, [1,2,3,4,5,6]))
print(bestSum(113, [10,19,17,70]))

