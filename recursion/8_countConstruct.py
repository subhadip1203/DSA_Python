
def wordMatch(targetWord,subWord):
    targetWordLength = len(targetWord)
    subWordLength = len(subWord)
    if targetWordLength - subWordLength < 0:
        return False
    for i in range (subWordLength) :
        if subWord[i] != targetWord[i] :
            return False
    
    return targetWord[subWordLength:]


def canConstruct(targetWord, wordBank):
    if targetWord == "" : return True
    countNo = 0
    for word in wordBank:
        restOfString = wordMatch(targetWord,word)
        if restOfString != False:
            returnData = canConstruct(restOfString, wordBank)
            if returnData != False:
                countNo = countNo+ 1
    
    return countNo

print(canConstruct("abcdefghi",["abc","d","efg","h","i"]))
print(canConstruct("purple",["le","pu","p","pur","ple"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e","ee","eeee","eeeee","eeeeeeee","eeeeeeeeee"
]))