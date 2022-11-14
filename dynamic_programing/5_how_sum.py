
def howSum(num, arr, memo={}):
    if memo.get(num) : return memo[num]
    if num == 0: return []
    if num < 0 : return None

    for x in arr:
        reminder = num-x
        reminderResult = howSum(reminder,arr,memo)
        if reminderResult != None:
            reminderResult.append(x)
            memo[reminder] = reminderResult
            return reminderResult
    return None

print(howSum(7,[3,5,2]))