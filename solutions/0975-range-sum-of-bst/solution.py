# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        valid_scores = []

        def helper(root, low, high):
            if not root:
                return
            
            if low <= root.val <= high:
                valid_scores.append(root.val)
            
            if root.val >= low:
                helper(root.left, low, high)
            
            if root.val <= high:
                helper(root.right, low, high)
        
        helper(root, low, high)

        return sum(valid_scores)

        
