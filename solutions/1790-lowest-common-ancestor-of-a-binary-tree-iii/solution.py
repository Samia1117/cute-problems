"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:

    def find_root(self, node):

        if not node:
            return None
        if node.parent == None:
            return node
        
        return self.find_root(node.parent)

    def has_p_or_q(self, node, p, q):
        if not node:
            return None

        left = self.has_p_or_q(node.left, p, q)
        right = self.has_p_or_q(node.right, p, q)

        if left and right:
            return node
        else:
            if node.val == p.val or node.val == q.val:
                return node
            if left:
                return left
            if right:
                return right

    @cache
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        root = self.find_root(p)

        return self.has_p_or_q(root, p, q)

        # has_q = self.has_node(p.left, q.val)
        # if not has_q:
        #     has_q = self.has_node(p.right, q.val)

        # if has_q:
        #     return p.val

        # has_p = self.has_node(q.left, p.val)
        # if not has_p:
        #     has_p = self.has_node(q.right, p.val)

        # if has_p:
        #     return q.val



        
        
        
