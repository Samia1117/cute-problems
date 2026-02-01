from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ret = {}

        def _dfs(root: Optional[TreeNode], data: dict, level: int) -> None:
            if not root:
                return
            if level not in data:
                data[level] = []
            data[level].append(root.val)
            _dfs(root.left, data, level+1)
            _dfs(root.right, data, level+1)

        _dfs(root, ret, 0)
        
        formatted = ret.values()
        # print(f'Values = {formatted}')
        return list(formatted)
