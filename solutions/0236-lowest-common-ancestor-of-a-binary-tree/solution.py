# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, p, q):
            if not root:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root
            
            found_left = helper(root.left, p, q)
            found_right = helper(root.right, p, q)

            if found_left and found_right:
                return root
            
            if found_left:
                return found_left
            
            if found_right:
                return found_right

            return None
        
        return helper(root, p, q)
