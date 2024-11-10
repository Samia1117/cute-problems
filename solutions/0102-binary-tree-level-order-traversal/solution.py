# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def populate_dict(self, root, level_dict, level):

        if not root:
            return

        if level not in level_dict:
            level_dict[level] = []
        
        level_dict[level].append(root.val)

        self.populate_dict(root.left, level_dict, level+1)
        self.populate_dict(root.right, level_dict, level+1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_dict = {}
        self.populate_dict(root, level_dict, 0)
        sorted_by_level = sorted(level_dict.items(), key=lambda x: x[0])

        return [x[1] for x in sorted_by_level]

        


        
