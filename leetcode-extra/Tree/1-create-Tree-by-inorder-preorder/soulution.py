# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # if no value , then return None
        if preorder == None or inorder == None :
            return None
        if len(preorder) == 0 or len(inorder) == 0 :
            return None

        # get the first index value of preorder and create a tree
        root_val = preorder[0]
        result_tree = TreeNode(root_val)
    
        # find index in in-order array
        index = inorder.index(root_val)
      
        # new preorder for leftside and rightside
        left_preorder = preorder[1:index+1]
        right_preorder = preorder[index+1:]

        # new inorder
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]


        # making left and side tree
        result_tree.left = self.buildTree(left_preorder , left_inorder)
        result_tree.right = self.buildTree(right_preorder , right_inorder)

        # return tree
        return result_tree