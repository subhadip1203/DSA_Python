
def howSum(num, arr, memo={}):
    if memo.get(num) : return memo[num]
    if num == 0: return []
    if num < 0 : return None

    for x in arr:
        reminder = num-x
        reminderResult = howSum(reminder,arr,memo)
        memo[reminder] = reminderResult
        if reminderResult != None:
            reminderResult.append(x)
            return reminderResult
    return None

print(howSum(300,[3,5,2]))