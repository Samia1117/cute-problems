class Solution:

    def isInBounds(self, row, col, maxRow, maxCol):

        if row < 0 or row >= maxRow:
            return False
        if col < 0 or col >= maxCol:
            return False

        return True
    
    def getUid(self, row, col, maxCol):
        return row * maxCol + col

    def getRowColFromId(self, uid, maxCol):
        row = uid // maxCol # 5 // 3 = 1
        col = uid % maxCol  # 5 % 3 = 2
                            # So row = 1, col = 2

        return [row, col]
    
    '''
    Checks if elt at row,col will rot at this timestep
    '''
    def will_rot(self, rotten, row, col, max_row, max_col):
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for delta in deltas:
            row_delta = delta[0]
            col_delta = delta[1]
            if self.isInBounds(row + row_delta, col + col_delta, max_row, max_col):
                if (row + row_delta, col + col_delta) in rotten:
                    return True # this cell will also rot

        return False


    def orangesRotting(self, grid: List[List[int]]) -> int:

        max_row = len(grid)
        if max_row == 0:
            return -1
        max_col = len(grid[0])

        rotten = set()
        not_rotten = set()
        neutral = set()

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == 2:
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    not_rotten.add((i, j))
                else:
                    neutral.add((i, j))
        
        iters = 0
        max_iters = max_row * max_col
        prev_rotten_length = len(rotten)

        # Iterate through the 'non-rotten' and pull changes from its rotten neighbors
        while iters < max_iters:
            # print(f"rotten oranges = {rotten}, non_rotten = {not_rotten}")
            will_rot_this_timestep = set()
            for elt in not_rotten:
                if self.will_rot(rotten, elt[0], elt[1], max_row, max_col):
                    will_rot_this_timestep.add(elt)
            not_rotten = not_rotten - will_rot_this_timestep
            rotten.update(will_rot_this_timestep)
            if len(rotten) == prev_rotten_length:   # if there was no change since last time step
                break
            prev_rotten_length = len(rotten)
            iters += 1
        
        if len(not_rotten) > 0: # if we were left with some oranges that did not rot
            return -1
        
        return iters








        
