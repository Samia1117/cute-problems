class TicTacToe:

    # self.hmap = {}

    def is_winning_condition_reached(self, player):
        # print(self.hmap)

        # if len(self.hmap[player]) < self.n:
        #     return False

        rows = self.hmap[player][0]
        cols = self.hmap[player][1]

        print("Player = ", player)
        print("rows: ", rows.items())
        for row_tuple in rows.items():
            if row_tuple[1] >= self.n:
                return True

        print("cols: ", cols.items())
        for col_tuple in cols.items():
            if col_tuple[1] >= self.n:
                return True

        # diagonal
        print("diagmap1: ", self.diagmap1)
        print("diagmap2: ", self.diagmap2)

        if player in self.diagmap1:
            if self.diagmap1[player] >= self.n:
                return True
        if player in self.diagmap2:
            if self.diagmap2[player] >= self.n:
                return True
            
        # for i in range(self.n):
        #     moves = self.hmap[player]
        #     m = len(moves)
        #     # horizontal
        #     row_i = [moves[k] for k in range(m) if moves[k][0] == i]
        #     # vertical
        #     col_i = [moves[k] for k in range(m) if moves[k][1] == i]

        #     if len(row_i) >= self.n or len(col_i) >= self.n:
        #         return True

        # Check the two diagonals
        # diag_1 = len([moves[k] for k in range(self.n) if moves[k][0] == moves[k][1]])
        # diag_2 = len([moves[k] for k in range(self.n) if moves[k][0] + moves[k][1] == (self.n - 1)])

        # if diag_1 >= self.n or diag_2 >= self.n:
        #     return True
            
        return False

    def __init__(self, n: int):
        self.n = n
        self.grid = [[[] for i in range(n)] for j in range(n)]

        self.hmap = {}
        self.diagmap1 = {}
        self.diagmap2 = {}

    def move(self, row: int, col: int, player: int) -> int:

        if player not in self.hmap: 
            # first move from this player
            self.hmap[player] = [{}, {}]
        if row not in self.hmap[player][0]:
            self.hmap[player][0][row] = 0
        self.hmap[player][0][row] += 1
        if col not in self.hmap[player][1]:
            self.hmap[player][1][col] = 0
        self.hmap[player][1][col] += 1

        if row == col:
            if player not in self.diagmap1:
                self.diagmap1[player] = 0
            self.diagmap1[player] += 1

        if row + col == (self.n - 1):
            if player not in self.diagmap2:
                self.diagmap2[player] = 0
            self.diagmap2[player] += 1

        # print(self.hmap)
        # self.hmap[player].append([row, col])

        if self.is_winning_condition_reached(player):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
