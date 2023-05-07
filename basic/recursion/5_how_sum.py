
def howSum(num, arr):
    if num == 0: return []
    if num < 0 : return None

    for x in arr:
        reminder = num-x
        reminderResult = howSum(reminder,arr)
        if reminderResult != None:
            reminderResult.append(x)
            return reminderResult
    return None

print(howSum(7,[3,5,3]))