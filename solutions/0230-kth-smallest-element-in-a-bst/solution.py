# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def node_arr(self, root, arr):
        if root == None:
            return arr
        arr.append(root.val)
        if root.right != None:
            right_nodes = self.node_arr(root.right, arr)
        if root.left != None:
            left_nodes = self.node_arr(root.left, arr)
            
        return arr
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        all_nodes_arr = self.node_arr(root, arr)
        sorted_arr = sorted(all_nodes_arr)
        print(sorted_arr)
        
        return sorted_arr[k-1]
