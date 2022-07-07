# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return None
        invertedRight = self.invertTree(root.right)
        invertedLeft = self.invertTree(root.left)
        root.left = invertedRight
        root.right = invertedLeft
        return root
        
            
            
