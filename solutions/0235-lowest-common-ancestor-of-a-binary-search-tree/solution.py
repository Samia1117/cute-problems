# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left == None and right == None):
            return
        
        if (left != None and right != None ):
            return root

        if left == None:
            return right

        if right == None:
            return left
        
        # if left == p and right == q (or vice versa), then lca = root
        # else, if left != null and right == null, no lca on right side, 
        # if left == null and right == null, then lca = null
        # if left != n
