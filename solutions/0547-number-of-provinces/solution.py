class Solution:

    # def dfs(self, v, adj_dict, seen):
    #     if v in seen:
    #         return
    #     seen.add(v)
    #     for neighbor in adj_dict[v]:
    #         if neighbor not in seen:
    #             self.dfs(neighbor, adj_dict, seen)

    def dfs(self, v, isConnected, seen):
        if seen[v]:
            return
        seen[v] = True

        for w in range(len(isConnected)):
            if isConnected[v][w] and not seen[w]:
                self.dfs(w, isConnected, seen)
        return 

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        if n == 0:
            return 0

        # adj_dict = {}
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j] == 1:
        #             if i not in adj_dict:
        #                 adj_dict[i] = set()
        #             if j not in adj_dict:
        #                 adj_dict[j] = set()
        #             adj_dict[i].add(j)
        #             adj_dict[j].add(i)
        # print(f'adj_dict={adj_dict}')

        num_provinces = 0
        seen = [False for i in range(n)]

        for i in range(n):
            if not seen[i]:
                num_provinces += 1
                self.dfs(i, isConnected, seen)

        return num_provinces
        '''
        seen = set()
        last_seen = set()

        for key in adj_dict.keys():
            self.dfs(key, adj_dict, seen)
            # print(f"seen {seen}")
            # print(f"last_seen {last_seen}")
            if len(last_seen) < len(seen):
                num_provinces += 1
                last_seen = seen.copy()

        return num_provinces
        '''

        
