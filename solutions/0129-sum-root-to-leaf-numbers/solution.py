# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, nums, root, current_cnt):
        if root == None:
            return 
        if root.left == None and root.right == None:
            current_cnt += str(root.val)
            nums.append(current_cnt)
            return 
        else:
            current_cnt += str(root.val)
            self.traverse(nums, root.left, current_cnt )
            self.traverse(nums, root.right, current_cnt)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        nums = []
        self.traverse(nums, root, "")
        print("Nums is = ", nums)
        nums_int = [int(x) for x in nums]

        return sum(nums_int)
        
        

        
        
