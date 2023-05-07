
def bestSum (num, arr):
    if num == 0 : return []
    if num < 0  : return None

    result = None

    for x in arr:
        reminder = num-x
        reminderArr = bestSum (reminder, arr)
        if reminderArr != None:
            newArr = [x, *reminderArr]
            if result == None or   len(newArr) < len(result) :
                result = newArr

    return result

print(bestSum(11, [1,2,3,4,5,6]))
print(bestSum(110, [1,2,3,4,5,6]))

