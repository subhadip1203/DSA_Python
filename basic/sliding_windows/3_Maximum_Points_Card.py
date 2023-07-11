"""
Leetcode : https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


video : https://www.youtube.com/watch?v=TsA4vbtfCvo&t=491s
"""

class Solution:
    def maxScore(self, cardPoints, k):
       
        result = 0
        for i in range(k):
            result += cardPoints[i]

        previousResult = result
        i = 1 
        while i <= k:
            previousResult = previousResult - cardPoints[k-i]+ cardPoints[len(cardPoints) -i]
            result = max(result,previousResult)
            i += 1

        return result


cardPoints = [1,2,3,4,5,6,1]
k = 3
print( Solution().maxScore(cardPoints,k))