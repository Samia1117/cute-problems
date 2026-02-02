# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balanced_and_height(root):
            if not root:
                return True, 0
            
            left_is_balanced, left_height = check_balanced_and_height(root.left)
            if not left_is_balanced:
                return False, None
                        
            right_is_balanced, right_height = check_balanced_and_height(root.right)
            if not right_is_balanced:
                return False, None
            
            return (abs(left_height - right_height) <= 1, 1 + max(left_height, right_height))
        
        is_balanced, height = check_balanced_and_height(root)
        return is_balanced

        # def _height(root: Optional[TreeNode]) -> list[int]:

        #     if not root:
        #         return 0
            
        #     return 1 + max(_height(root.left), _height(root.right))
        
        # if not root:
        #     return True
        
        # return self.isBalanced(root.left) and self.isBalanced(root.right) and (
        #     abs(_height(root.right) - _height(root.left)) <= 1
        # ) 
            
        
            
        
