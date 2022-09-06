# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBSTUtil(self, node, minVal, maxVal):
        
        if node == None:
            return True

        if (node.val >= maxVal or node.val <= minVal):
            return False
        
        return self.isValidBSTUtil(node.left, minVal, node.val) and self.isValidBSTUtil(node.right, node.val, maxVal)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
            
        return self.isValidBSTUtil(root, -sys.maxsize, sys.maxsize)
        
