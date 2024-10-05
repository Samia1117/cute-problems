class Solution:
    def median(self, alist: List[int]) -> int:
        if not alist:
            return None
        if len(alist) == 1:
            return alist[0]
        
        n = len(alist)
        alist = sorted(alist)
        if n%2 == 0:
            return alist[int(n/2)]
        else:
            return alist[int((n-1)/2)]

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        friend_locs = []

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            row = grid[i]
            for j in range(m):
                if grid[i][j] == 1:
                    friend_locs.append([i, j])

        #x_bar = int(sum([x[0] for x in friend_locs])/len(friend_locs) )
        #y_bar = int(sum(x[1] for x in friend_locs)/len(friend_locs) )

        median_x = self.median([x[0] for x in friend_locs])
        median_y = self.median([x[1] for x in friend_locs])

        x_dist = sum([abs(median_x-x[0]) for x in friend_locs])
        y_dist = sum( [ abs(median_y-x[1]) for x in friend_locs] )

        return x_dist + y_dist
        
