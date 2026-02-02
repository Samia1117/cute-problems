# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(root, curr_sum, target_sum):

            if not root:
                return False
            
            curr_sum += root.val
            if not root.left and not root.right: # need to meet leaf condition
                return curr_sum == target_sum
            
            return helper(root.left, curr_sum, target_sum) or helper(root.right, curr_sum, target_sum)
        
        if not root:
            return False

        return helper(root, 0, targetSum)


        
