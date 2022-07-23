# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDiam = 0
        
        def depth(tnode):
            if not tnode:
                return 0
            maxDepthLeft = depth(tnode.left)
            maxDepthRight = depth(tnode.right)
            
            self.maxDiam = max(self.maxDiam, maxDepthLeft + maxDepthRight)
            return 1 + max(maxDepthLeft, maxDepthRight)
        
        depth(root)
        # print(self.maxDiam)
        return self.maxDiam
        
