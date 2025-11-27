class Solution:
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    def minKnightMoves(self, x: int, y: int) -> int:

        '''
        q = deque()
        q.append((0, 0, 0)) # x, y, distance
        visited = set()

        while q:
            popped = q.popleft()
            i, j, num_moves = popped[0], popped[1], popped[2]
            if i == x and j == y:
                return num_moves
            for move in Solution.moves:
                next_i, next_j = i + move[0], j + move[1]
                if (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    q.append((next_i, next_j, num_moves + 1))
                    
        return sys.maxsize
        '''

        # Solution 2
        source_q = deque([(x, y)]) # x, y, distance to (x,y)
        source_dist = {(x, y): 0}

        target_q = deque([(0, 0)])   # 0, 0, distance to (0,0)
        target_dist = {(0, 0): 0}

        while source_q and target_q: # solution is guaranteed to exist
            sq_elt = source_q.popleft()
            source_i, source_j = sq_elt[0], sq_elt[1]
            if (source_i, source_j) in target_dist:
                return source_dist[(source_i, source_j)] + target_dist[(source_i, source_j)]
            
            tq_elt = target_q.popleft()
            target_i, target_j = tq_elt[0], tq_elt[1]
            if (target_i, target_j) in source_dist:
                return source_dist[(target_i, target_j)] + target_dist[(target_i, target_j)]
            
            for move in Solution.moves:
                next_source_i, next_source_j = source_i + move[0], source_j + move[1]
                next_target_i, next_target_j = target_i + move[0], target_j + move[1]

                if (next_source_i, next_source_j) not in source_dist:
                    source_dist[(next_source_i, next_source_j)] = source_dist[(source_i, source_j)] + 1
                    source_q.append((next_source_i, next_source_j))

                if (next_target_i, next_target_j) not in target_dist:
                    target_dist[(next_target_i, next_target_j)] = target_dist[(target_i, target_j)] + 1
                    target_q.append((next_target_i, next_target_j))
        
        return sys.maxsize

        
