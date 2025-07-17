# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2):

        if root1 == None and root2 == None:
            return True

        if root1 != None and root2 != None:
            if root1.val == root2.val:
                right = self.isSameTree(root1.right, root2.right)
                left = self.isSameTree(root1.left, root2.left)
                return left and right
            else:
                return False
        else:
            return False

    def dfs(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root:
            # print(f'root = {root}, subroot = {subRoot}')
            return False

        if self.isSameTree(root, subRoot):
            return True
        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
