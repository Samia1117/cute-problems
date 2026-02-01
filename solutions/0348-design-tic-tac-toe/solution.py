class TicTacToe:

    def __init__(self, n: int):
        self.grid = [[0 for i in range(n)] for j in range(n)]
        self.player_moves = {}
        self.n = n
    
    def _check_winning_condition(self, player: int) -> bool:
        n = self.n
        grid = self.grid 

        for i in range(n):
            sum_row_i = sum(grid[i])
            if abs(sum_row_i) == n:
                return player
            sum_col_i = sum([grid[k][i] for k in range(n)])
            if abs(sum_col_i) == n:
                return player
        
        # Check diagonals
        if abs(sum([grid[i][i] for i in range(n)])) == n:
            return player
        
        if abs(sum([grid[i][n-i-1] for i in range(n)])) == n:
            return player

        return 0


    def move(self, row: int, col: int, player: int) -> int:
        # if player not in self.player_moves:
        #     self.player_moves[player] = {}


        if self.grid[row][col] == 0: # otherwise invalid move
            if player == 1:
                self.grid[row][col] = -1
            else:
                self.grid[row][col] = 1
            # print(f'grid = {self.grid}')
            return self._check_winning_condition(player)
        else:
            # print(f'grid = {self.grid}')
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
