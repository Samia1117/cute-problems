import numpy as np

class Solution:

    def dfs(self, node, rooms, visited):
        if visited[node]:
            return
        visited[node] = True
        return

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # create adjacency matrix
        d = {}
        n = len(rooms)
        for i in range(n):
            d[i] = rooms[i]

        print("dict: ", d)

        visited = [False for i in range(n)]

        stack = deque()
        stack.append(0) # can visit room 0
        # visited = set([])

        while stack:
            print("stack", stack)
            popped = stack.pop()
            visited[popped] = True

            neighbors = d[popped]
            for neigh in neighbors:
                if visited[neigh] == False:
                    stack.append(neigh)
        
        for i in range(n):
            if not visited[i]:
                return False
        return True


        
