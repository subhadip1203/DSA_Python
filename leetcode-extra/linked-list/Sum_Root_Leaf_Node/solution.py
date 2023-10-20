# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def sumNumbers(root):

    answer = 0
    currentNum = 0

    # recursion func
    def  calculateSum(node,currentNum):
        nonlocal answer
        currentNum = currentNum*10 + node.val
        if node.left == None and node.right == None:
            print('adding',currentNum)
            answer = answer+ currentNum
        else:
            if node.left != None:
                calculateSum(node.left,currentNum)
            if node.right != None:
                calculateSum(node.right,currentNum)
    
    
    # calling the function of root
    calculateSum(root, currentNum)
    
    return answer




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sumNumbers(root))





root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(sumNumbers(root))

