
def Palindrome(str):
    strLen = len(str)
    if len(str) == 0:
        return True
    if len(str) == 1:
        return True
    else:
        index = strLen-1
        print(str[0],str[index])
        if str[0].lower() == str[index].lower():
            return Palindrome(str[1:index])
        return False

myStr = "Neveroddoreven"
print(Palindrome(myStr))