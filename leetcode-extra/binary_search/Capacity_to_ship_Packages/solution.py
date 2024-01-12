
#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights, days):

        def canShip(weights , days , ship_capacity):
            dayVal = 1
            currentCapacity = 0
            for item in weights:
                if currentCapacity + item > ship_capacity:
                    dayVal += 1
                    currentCapacity = 0
                currentCapacity += item
            
            return True if dayVal <= days else False



        maxVal = weights[0]
        sumVal = weights[0]

        for i in range(1,len(weights)):
            maxVal = max(maxVal,weights[i])
            sumVal += weights[i]

        minCap = maxVal
        maxcap = sumVal
        
        while minCap < maxcap:
            midVal = (minCap + maxcap)//2

            if canShip(weights , days , midVal) :
                maxcap = midVal
            else:
                minCap = midVal + 1
        
        return maxcap



        

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights,days))


weights = [3,2,2,4,1,4] 
days = 3
print(Solution().shipWithinDays(weights,days))