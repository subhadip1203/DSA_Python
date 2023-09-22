
class Solution:
    def pathSum(self, root, targetSum) :

        memo = {}
        self.result = 0

        def dfs(node , currentSum , targetSum):
        
            if node:
                currentSum += node.val
                difference = currentSum - targetSum
                
                self.result  += memo[difference] 
                
                memo[currentSum]  += 1

                dfs(node.left , currentSum , targetSum)
                dfs(node.right , currentSum , targetSum)


                memo[currentSum]  -= 1
            
        
        dfs(root , 0 , targetSum)
        return self.result