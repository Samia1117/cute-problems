#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root.left == None:
            if root.right==None:  # leaf node
                return root
            else:
                right_subtree = self.invertTree(root.right)
                root.left = right_subtree # right side not empty
                root.right = None
                return root
        if root.right == None:
            left_subtree = self.invertTree(root.left)
            root.right = left_subtree # left not None
            root.left = None
            return root
        
        if root.left.left == None and root.left.right == None and root.right.right == None and root.right.left==None:
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
            
        else:
            my_left = self.invertTree(root.left)
            my_right = self.invertTree(root.right)
            
            temp = my_left
            root.left = my_right
            root.right = temp
            return root
        
