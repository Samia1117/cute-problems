"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        '''
        Description was hella confusing
        Just find the root node - could be anywhere in the list
        '''
        if not tree:
            return None

        adj_dict = {}
        for node in tree:
            if node.val not in adj_dict:
                adj_dict[node.val] = [0, node]

            for child in node.children:
                if child.val not in adj_dict:
                    adj_dict[child.val] = [0, node]
                adj_dict[child.val][0] += 1 # increment indegree node -> right

            # right = node.right
            # if right != None:
            #     if right.val not in adj_dict:
            #         adj_dict[right.val] = 0
            # adj_dict[right.val] += 1 # increment indegree node -> right

        # print(f'adj_dict with indegree ={adj_dict}')
        res = [v[1] for v in adj_dict.values() if v[0] == 0]
        # print(f'Candidate keys = {res}')
        return res[0]

