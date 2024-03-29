# def wordMatch(targetWord,subWord):
#     targetWordLength = len(targetWord)
#     subWordLength = len(subWord)
#     if targetWordLength - subWordLength < 0:
#         return False
#     for i in range (subWordLength) :
#         if subWord[i] != targetWord[i] :
#             return False
    
#     return targetWord[subWordLength:]


def canConstruct(targetWord, wordBank, memo=None):
    if memo == None:
        memo = {}

    if targetWord in memo:
        return memo[targetWord]
    elif targetWord == "":
        return True
    
    for word in wordBank:
       if word in targetWord :
            restOfString = targetWord[len(word):]
            returnData = canConstruct(restOfString, wordBank, memo)
            if returnData:
                memo[targetWord] = True
                return True

    memo[targetWord] = False
    return False


print(canConstruct("abcdefghi", ["abc", "d", "efg", "h", "i"]))
print(canConstruct("purple", ["le", "pu", "p", "pur", "ple"]))
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
