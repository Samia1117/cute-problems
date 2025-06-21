# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def populate(self, root, level, dic) -> None:

        if not root:
            return
        if level not in dic:
            dic[level] = []

        dic[level].append(root.val)
        self.populate(root.left, level+1, dic)
        self.populate(root.right, level+1, dic)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        dic = {}
        self.populate(root, 0, dic)
        # print(f"dic = {dic}")
        
        res = []
        for key in reversed(dic.keys()):
            res.append(dic[key])
        return res
