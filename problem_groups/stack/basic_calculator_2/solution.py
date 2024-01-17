# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/description/
# video = https://www.youtube.com/watch?v=gmy6L9vHTbo



class Solution:
    def calculate(self, s) :

        stack = []
        currentNum = 0
        currentSign  = '+'

        i = 0
        while i < len(s) :

            # if current char in number
            if s[i].isdigit():
                tempNum = 0
                while i < len(s) and s[i].isdigit():
                    tempNum = tempNum * 10 + int(s[i])
                    i+= 1
                i -= 1

                currentNum  = tempNum

                if currentSign == '-':
                    negativeNum = currentNum*-1
                    stack.append(negativeNum)
                elif currentSign == '*':
                    lastnum = stack.pop()
                    multipledNum = lastnum * currentNum
                    stack.append(multipledNum)
                elif currentSign == '/':
                    lastnum = stack.pop()
                    devideNum = int(lastnum / currentNum)
                    stack.append(devideNum)
                else:
                    stack.append(currentNum)

            elif s[i] == '+':
                currentSign  = '+'
                currentNum  = 0
            
            elif s[i] == '-':
                currentSign  = '-'
                currentNum  = 0

            elif s[i] == '*':
                currentSign  = '*'
                currentNum  = 0

            elif s[i] == '/':
                currentSign  = '/'
                currentNum  = 0

            i += 1

        result = 0
        for item in stack:
            result += item
        
        return(result)


s = "3+2*2"
print( Solution().calculate(s) )

s = " 3+5 / 2 + 3 - 4*3"
print( Solution().calculate(s) )