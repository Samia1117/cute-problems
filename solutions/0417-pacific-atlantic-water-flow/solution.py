class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacifics = set()
        atlantics = set()
        seen = set()

        def in_range(i, j):
            if i < 0 or j < 0:
                return False
            if i >= max_row or j >= max_col:
                return False

            return True
        

        # def canFlow(i, j) -> bool:
        #     def in_range(i, j):
        #         if i < 0 or j < 0:
        #             return False
        #         if i >= max_row or j >= max_col:
        #             return False

        #         return True

        #     # return whether water from heights[i][j] can flow into both Pacific and Atlantic
        #     # How to do this? Start a bfs from heights[i][j]. If can reach row 0 or column 0 -> Pacific; if can reach row n or column n -> Atlantic

        #     q = deque()
        #     visited = set()
        #     q.append((i, j))

        #     deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     pacific = False
        #     atlantic = False

        #     while q:
        #         row, col = q.popleft()
        #         visited.add((row, col))
        #         # print(f'row, col = {row, col}')

        #         if row == 0 or col == 0:
        #             pacific = True
        #         if row == max_row - 1 or col == max_col - 1:
        #             atlantic = True
                
        #         if pacific and atlantic:
        #             return True

        #         for i in range(4):
        #             neigh_i, neigh_j = deltas[i][0] + row, deltas[i][1] + col

        #             if (neigh_i, neigh_j) not in visited and in_range(neigh_i, neigh_j) and heights[neigh_i][neigh_j] <= heights[row][col]:
        #                 q.append((neigh_i, neigh_j)) 
        #     return False
        def bfs(q, visited):
            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                row, col = q.popleft()
                visited.add((row, col))

                for i in range(4):
                    neigh_i, neigh_j = deltas[i][0] + row, deltas[i][1] + col
                    if (neigh_i, neigh_j) not in visited and in_range(neigh_i, neigh_j) and heights[neigh_i][neigh_j] >= heights[row][col]:
                        q.append((neigh_i, neigh_j)) 
            # print(f'visited = {visited}')
            return visited

        if len(heights) == 0 or len(heights[0]) == 0:
            return False

        max_row, max_col = len(heights), len(heights[0])
        result = []

        dp = [[0 for i in range(max_col)] for j in range(max_row)]
        # 0 -> neither, 1 -> Pacific, 2 -> Atlantic

        pq = deque()
        aq = deque()

        for i in range(max_row):
            pq.append((i, 0))
            aq.append((i, max_col-1))
        
        for j in range(max_col):
            pq.append((0, j))
            aq.append((max_row-1, j))

        visited_p = set()
        visited_a = set()

        visited_p = bfs(pq, visited_p)
        visited_a = bfs(aq, visited_a)
        
        # for i in range(1, max_row):
        #     for j in range(1, max_col):
        #         if canFlow(i, j):
        #             # print(f"Can flow: {i, j}")
        #             result.append((i, j))

        # print(f'visited p = {visited_p}')
        # print(f'visited a = {visited_a}')

        for p in visited_p:
            if p in visited_a:
                result.append(p)

        return result
