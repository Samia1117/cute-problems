# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        paths = []
        def recurse(root, path_sum, global_sum):
            if root:
                path_sum = path_sum * 10 + int(root.val)
                # print(f'curr_sum = {curr_sum}')

                if not root.left and not root.right:
                    global_sum[0] += path_sum
                    return
                
                recurse(root.left, path_sum, global_sum) 
                recurse(root.right, path_sum, global_sum)
        
        # current_path = []
        global_sum = [0]
        recurse(root, 0, global_sum)

        return global_sum[0]
        
        # print(f'paths = {paths}')

        # return sum([sum(path) for path in paths])
            


