# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        # main idea is: if my right and left both return not none values, then either p or q is on right and the other on left
        # in that case, i should return the  root

        # otherwise, either left or right is none - so just return the side that's not none
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        return right
        
#         if root in (p, q, None):
#             return root
#         r,l = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
        
#         if r and l:
#             return root
#         if not r:
#             return l
#         return r
        
#         st = deque()
#         st.append(root)
#         visited = set()
        
#         while st:
#             p = st.pop()
            
            
        
        
