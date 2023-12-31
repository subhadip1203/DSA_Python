# https://leetcode.com/problems/largest-rectangle-in-histogram/description/


class Solution:
    def largestRectangleArea(self, heights):
        
        #left arrey for calculating smallest left side
        # left most part will be the smallet
        left = [0  for _ in heights]
        myStack =[]

        for i in range (len(heights)):

            if len(myStack) == 0:
                left[i] = 0
            else:
                while len(myStack) > 0 and heights[myStack[-1]] >= heights[i]:
                    myStack.pop()
                left[i] = 0 if len(myStack) == 0 else myStack[-1]+1
            
            myStack.append(i)

        # clear the stack
        myStack =[]
        right = [0  for _ in heights]

        for i in reversed(range (len(heights))):
            if len(myStack) == 0:
                right[i] = len(heights)-1
            else:
                while len(myStack) > 0 and heights[myStack[-1]] >= heights[i]:
                    myStack.pop()
                right[i] = len(heights)-1 if len(myStack) == 0 else myStack[-1]-1
            myStack.append(i)


        maxArea = 0

        for i in range(len(heights)):
            currentArea= heights[i] * ( right[i] -left[i] + 1 )
            maxArea = max( maxArea , currentArea)

        return maxArea


heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))

heights = [2,4]
print(Solution().largestRectangleArea(heights))

