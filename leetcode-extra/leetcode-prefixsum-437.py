class Solution:
    def pathSum(self, root, targetSum) :

        self.count = 0

        # default table have value : 0 and frequency of 0 is 1
        prefix_sum_table = {
            0 : 1
        }
        
        def dfs(node, targetSum,curr_sum):
            if  node:
                
                curr_sum += node.val
                
                key = curr_sum - targetSum
                if key in prefix_sum_table:
                   self.count +=  prefix_sum_table[key] 
                
                prefix_sum_table[curr_sum]  = prefix_sum_table.get(curr_sum,0) + 1
                
                dfs(node.left, targetSum, curr_sum)
                dfs(node.right, targetSum, curr_sum)
                
                # before ending the step , we will decrese curr_sum from table
                prefix_sum_table[curr_sum] -= 1
        
        dfs(root, targetSum, 0)
        return self.count