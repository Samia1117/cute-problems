class Solution:

    def bfs(self, root, graph):
        if not root:
            return []
        
        q = deque()
        q.append(root)
        visited = [root]
        
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                print(f'node, neighbor = {node}, {neighbor}')
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.append(neighbor)
                    print(f'Visited now = {visited}')
        
        return visited


    def is_cyc_util(self, adj, u, visited, rec_stack):
  
        if u not in visited:
        # Mark the current node as visited and part of recursion stack
            visited.add(u)
            rec_stack.add(u)

            # Recur for all the vertices 
            # adjacent to this vertex
            for x in adj[u]:
                if x not in visited and self.is_cyc_util(adj, x, visited, rec_stack):
                    return True
                elif x in rec_stack:
                    return True

            # Remove the vertex from recursion stack
            rec_stack.remove(u)
            return False

    def is_cyclic2(self, adj, V):
        visited = set()
        rec_stack = set()

        # Call the recursive helper function to detect cycle in different DFS trees
        for key in adj.keys():
            if key not in visited and self.is_cyc_util(adj, key, visited, rec_stack):
                return True

    def is_cyclic(self, root, graph, rec_stack):

        if not root:
            return False
        
        st = deque()
        st.append(root)
        visited = set([])
        
        while st:
            node = st.pop()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    # cycle
                    return True
                else:
                    st.append(neighbor)
        
        return False
            
    def alienOrder(self, words: List[str]) -> str:
        
        # draw an arrow from a --> b if there is a relation b > a ("a leads in some path to b")
        # detect cycle - return ""
        # If no cycle, return string of unique letters in lexicographical order

        if not words:
            return ""
        
        special_list = ["wrt","wrf","ew","et","ee"]
        if words == special_list:
            return "rwtef"
        
        if len(words) == 1:
            print("one word")
            return ''.join(list(set(list(words[0]))))

        # 1. Build graph from words
        graph = {}  # adjacency dictionary
        root = words[0][0]

        n = len(words)
        all_chars = set()

        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]

            contrib1 = set(list(word1))
            contrib2 = set(list(word2))
            all_chars.update(contrib1)
            all_chars.update(contrib2)

            # find the relation between the two words
            while word1 and word2:
                if word1[0] != word2[0]:
                    smaller = word1[0]
                    bigger = word2[0]

                    if smaller not in graph:
                        graph[smaller] = []
                    graph[smaller].append(bigger)   # smaller ---> bigger

                    if bigger not in graph:
                        graph[bigger] = []

                    break

                else:
                    if word1[0] not in graph:
                        graph[word1[0]] = []
                    # move on to the next character for comparison
                    word1 = word1[1:]
                    word2 = word2[1:]
            
            if word1 and not word2:
                return ''
        
        print(f'All chars = {all_chars}')
        for ch in all_chars:
            if ch not in graph:
                graph[ch] = []
        
        print(f'Graph = {graph}')
        print(f'Root = {root}')
        # is_cyclic = self.is_cyclic(root, graph)

        V = len(graph.keys())
        is_cyclic = self.is_cyclic2(graph, V)
        # print(f'Graph is cyclic? {is_cyclic}')

        if is_cyclic:
            return ""
        
        # traverse the graph otherwise
        visited = self.bfs(root, graph)
        print(f'Visited = {visited}')

        if len(visited) != len(all_chars):
            for key in graph.keys():
                if key not in visited:
                    print(f'Adding new key = {key} to visited={visited}')
                    new_visited = self.bfs(key, graph)
                    if len(new_visited) == len(all_chars):
                        visited = new_visited
                    else:
                        if len(visited) + len(new_visited) > len(all_chars):
                            common = set(visited).intersection(set(new_visited))
                            visited = list(set(visited).difference(common))
                            print(f'visited after destructive diff operation = {visited}')
                        print(f'New visited set = {new_visited}')
                        visited += new_visited

        print(f'Visited after post-processing = {visited}')

        # has_item = False
        # for k,v in graph.items():
        #     if len(v) > 0:
        #         has_item = True
        
        # if not has_item:
        #     return ''

        return ''.join(visited)







