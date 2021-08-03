# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        if root.val == targetSum and root.right==None and root.left ==None:
            return True
        
        if root.right !=None:
            right = self.hasPathSum(root.right, targetSum-root.val)
            if right == True:
                return True
        if root.left !=None:
            left = self.hasPathSum(root.left, targetSum-root.val)
            if left == True:
                return True
        return False
        
