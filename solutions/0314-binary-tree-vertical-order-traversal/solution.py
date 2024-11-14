# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, depth, direction_val, graph):
        if not node:
            return
        
        if direction_val not in graph:
            graph[direction_val] = []
        
        graph[direction_val].append((depth, node.val))
        self.dfs(node.left, depth + 1, direction_val - 1, graph)
        self.dfs(node.right, depth + 1, direction_val + 1, graph)


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        graph = {}
        self.dfs(root, 0, 0, graph)
        # print(f'Graph = {graph.items()}')

        items = sorted(graph.items(), key=lambda x:x[0])    # sort by column order
        values = [item[1] for item in items]    # extract values of the dictionary (ignoring key=column order)
        # print(f"values = {values}")

        # function to map [[(3,4), (1,2)], [(5,6)] ] -> [[2, 4], [6]]
        def mapper(x):
            x = sorted(x, key=lambda x: x[0])
            vals = [y[1] for y in x]
            return vals

        mapped_values = list(map(mapper, values))
        return mapped_values





        
