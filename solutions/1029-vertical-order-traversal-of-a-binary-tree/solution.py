# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, depth, breadth, graph):
        
        if not node:
            return
        
        if breadth not in graph:
            graph[breadth] = []
        graph[breadth].append((depth, node.val))

        self.dfs(node.left, depth + 1, breadth - 1, graph)
        self.dfs(node.right, depth + 1, breadth + 1, graph)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        graph = {}

        self.dfs(root, 0, 0, graph)

        # First sort by breadth
        values = [x[1] for x in sorted(graph.items(), key=lambda x: x[0])]
        # print(f'List of (depth,node_val) sorted by column = {values}')
        # Now sort by depth + lexicographic value
        def mapper(x):  # input = [(x1,y1), (x3,y3), (x2,y2)] -> output: [y1, y2, y3]
            sort1 = sorted(x, key=lambda x: x[1])    # sort by value first
            sort2 = sorted(sort1, key=lambda x: x[0])   # Now sort by depth
            return [a[1] for a in sort2]

        sorted_values = list(map(mapper, values))
        # print(f'values after 2nd + 3rd sort = {sorted_values}')
        return sorted_values

        # print("graph = ", graph)

        '''
        q = deque()
        column_dict = {}

        q.append((root, 0))

        min_range = 0
        max_range = 0

        while q:
            node, column = q.popleft()
            if node:
                if column not in column_dict:
                    column_dict[column] = []
                column_dict[column].append(node.val)

                min_range = min(min_range, column)
                max_range = max(max_range, column)

                q.append((node.left, column-1))
                q.append((node.right, column+1))
        
        answer = []

        for col in range(min_range, max_range+1):
            answer.append(column_dict[col])   
        print(f'answer = {answer}') 
        return answer

        '''


            


        
