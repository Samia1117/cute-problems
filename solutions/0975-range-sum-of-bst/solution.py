# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr_sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = 0
            right_sum = 0
            if node.val > low:
                left_sum = dfs(node.left)
            if node.val < high:
                right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)

        # perform an in order traversal of the bst
        # if root < low, then don't bother traversing left
        # if root > high, then don't bother traversing right

        if not root:
            return 0

        ans = 0
        dfs(root)
        return ans

        
