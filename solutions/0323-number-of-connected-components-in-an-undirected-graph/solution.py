class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            seen.add(node)
            for neighbor in adj[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        adj = {i:[] for i in range(n)}

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        # print(f'adj = {adj}')

        seen = set()
        num_components = 0

        for i in range(n):
            if i not in seen:
                num_components += 1
                dfs(i)
                
        return num_components

        
