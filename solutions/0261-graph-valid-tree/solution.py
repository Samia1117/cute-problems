class Solution:
    def dfs_cycle(self, root, adj_dict, rec_stack, parent):
        # print("root = ", root)
        rec_stack.add(root)
        # print("rec stack = ", rec_stack)

        for neighbor in adj_dict[root]:
            # print("neighbor = ", neighbor)
            if neighbor == parent:
                continue
            if neighbor in rec_stack:
                return True
            val = self.dfs_cycle(neighbor, adj_dict, rec_stack, root)
            # print("val = ", val)
            if val:
                return True
            
        return False


    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n <= 0:
            return True

        adj_dict = {}

        for i in range(n):
            adj_dict[i] = []
        
        for edge in edges:
            v_in = edge[0]
            v_out = edge[1]
            adj_dict[v_in].append(v_out)
            adj_dict[v_out].append(v_in)
        
        # check for valid tree - no cycles
        # no cycles = no "back edges"
        # a "back edge" is one that points to a node that has been previously seen in the recursion stack

        rec_stack = set()
        parent = 0
        root = 0

        is_cyclic = self.dfs_cycle(root, adj_dict, rec_stack, parent)
        if (not is_cyclic and len(rec_stack) == n):
            return True
        return False



        

        
