# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrderRec(self, root, row, col, col_dict): 
        if not root:
            return

        if col not in col_dict:
            col_dict[col] = []
        col_dict[col].append((root.val, row))

        self.verticalOrderRec(root.left, row+1, col-1, col_dict)
        self.verticalOrderRec(root.right, row+1, col+1, col_dict)

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        col_dict = {}

        self.verticalOrderRec(root, 0, 0, col_dict)

        col_dict = sorted(col_dict.items())
        # print(f'col_dict = {col_dict}')

        ans = []
        for tup in col_dict:  # e.g. [(3, 0), (15, 2)]
            vals = sorted(tup[1], key=lambda x: x[1])
            ans.append([v[0] for v in vals]) # [3, 15]

        # print(f'ans = {ans}')
        return ans
