# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root: Optional[TreeNode]) -> int:

        if not root:
            return -10000, -10000
        # calculate pathsums based on whether input root was used or not
        use_root_rsum, not_root_rsum = self.helper(root.right)
        use_root_lsum, not_root_lsum = self.helper(root.left)

        # calculate max possible without using current root:
        max_with_root = max( 
            (max(use_root_rsum, use_root_lsum) + root.val), 
            root.val)
        # calc max value without using current root

        max_wo_root = max(
            # best you could do with child nodes
            max (
                max(use_root_rsum, not_root_rsum),
                max(use_root_lsum, not_root_lsum)
            ),
            # best you can do with both children plus yourself
            (root.val + use_root_rsum + use_root_lsum)
        )

        return max_with_root, max_wo_root

        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        a,b = self.helper(root)
        return max(a, b)

        '''

        if not root:
            return -10000

        right_pathsum = self.maxPathSum(root.right)
        left_pathsum = self.maxPathSum(root.left)

        total_pathsum = root.val + right_pathsum + left_pathsum

        if root.val < 0:
            return max(max(total_pathsum, right_pathsum), left_pathsum)
        else:
            right_and_root = root.val + right_pathsum
            left_and_root = root.val + left_pathsum
            right_left_and_root = root.val + right_pathsum + left_pathsum

            return max(max(right_and_root, left_and_root), right_left_and_root)
            '''
