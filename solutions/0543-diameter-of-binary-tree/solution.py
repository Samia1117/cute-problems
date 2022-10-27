# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.maxx = 0
    
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        #print("current max diam: {} + {} + 1".format(left, right) )
        self.maxx = max(self.maxx, left+right+1)
        #print("current maxHeight: ", 1 + max(left, right))
        return 1 + max(left, right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth(root)
        return self.maxx-1
        
