# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class maxSum:
    def __init__(self):
        self.val = -1000
        
class Solution:
    def maxPathSum2(self, root, maxSum):
        if root == None:
            return 0
        
        maxL = self.maxPathSum2(root.left, maxSum)
        maxR =  self.maxPathSum2(root.right, maxSum)
        if maxR<0:
            maxR = 0
        if maxL<0:
            maxL = 0
            
        if maxL+maxR+root.val >maxSum.val:
            maxSum.val = maxL+maxR+root.val
        return max(maxL+root.val, maxR+root.val)
                        
    def maxPathSum(self, root: TreeNode) -> int:
        if root.right == None and root.left == None:
            return root.val
        ms = maxSum()
        othermax = self.maxPathSum2(root, ms)
        print(othermax)
        return ms.val
            
        
