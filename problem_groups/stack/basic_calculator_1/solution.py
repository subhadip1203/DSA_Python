# Leetcode 224
# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s):
        
        sumVal = 0
        currentSign = 1 # plus sign = 1 , minus sign = -1
        stack = []

        i = 0
        while i < len(s):

            # for curent char is digit
            # run a while loop , till char are some number
            # after while loop decrese the i once ,
            # as the last i index will be "+","-","(", ")"

            if s[i].isdigit():
                tempNum = 0
                while i< len(s) and  s[i].isdigit():
                    tempNum = tempNum*10+int(s[i])
                    i+=1
                i-=1
                
                sumVal += tempNum * currentSign
                currentSign = 1
               
            
            elif s[i] == "-":
                currentSign = -1

            
            elif s[i] == "(":
                stack.append(sumVal)
                stack.append(currentSign)
                sumVal = 0
                currentSign = 1
            
            elif s[i] == ")":
                lastSignInStack = stack.pop()
                lastSumInStack = stack.pop()
                sumVal = lastSumInStack + sumVal * lastSignInStack

            i+= 1

        return sumVal


s = "1 + 1-(5+5) - 20+5"
print(Solution().calculate(s))