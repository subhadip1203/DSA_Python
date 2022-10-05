
def reverseStr(str):
    if len(str) == 1:
        return str
    lastindex = len(str)-1
    return str[lastindex]+reverseStr(str[:lastindex])
    

myStr = "abcde"
print(reverseStr(myStr))