# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # we add root first, then left child, then right child
    # if root is not null, then add root. Check left. Check right
    def level_order_arr(self, root, level, level_dict):
        if root == None:
            return
        
        if level not in level_dict:
            level_dict[level] = []
        level_dict[level].append(root.val)
        
        if root.left != None:
            self.level_order_arr(root.left, level+1, level_dict)
        if root.right != None:
            self.level_order_arr(root.right, level+1, level_dict)
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_dict = {}
        level = 0
        self.level_order_arr(root, level, level_dict)
        
        sorted_level_tup = sorted(level_dict.items(), key=lambda x: x[0])
        #print(sorted_level_tup)
        larr = []
        for tup in sorted_level_tup:
            larr.append(tup[1])
        #print(larr)
        return larr
        
