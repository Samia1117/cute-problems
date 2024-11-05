import copy

class Solution:

    @staticmethod
    def score(i, j, maxcol):
        return i * maxcol + j

    def matches(self, i, j, grid, word, visited):

        # print("Char, word = ", [grid[i][j], word])
        
        if len(word) == 0:
            return True

        if grid[i][j] != word[0]:
            return False
        else:
            if grid[i][j] == word[0] and len(word) == 1:
                return True
        
        # print("At char, remainig word = ", [grid[i][j], word])
        # print("visited: ", visited)
        
        up = False
        down = False
        right = False
        left = False

        visited.add(self.score(i, j, self.col_len))

        if i > 0 and not self.score(i-1, j, self.col_len) in visited:
            up = self.matches(i-1, j, grid, word[1:], visited)
        if j > 0 and not self.score(i, j-1, self.col_len) in visited:
            left = self.matches(i, j-1, grid, word[1:], visited)
        if i < self.row_len - 1 and not self.score(i+1, j, self.col_len) in visited:
            down = self.matches(i+1, j, grid, word[1:], visited)
        if j < self.col_len - 1 and not self.score(i, j+1, self.col_len) in visited:
            right = self.matches(i, j+1, grid, word[1:], visited)

        visited.remove(self.score(i, j, self.col_len))

        if up or down or left or right:
            # print("Matched = ", [up, down, left, right])
            return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row_len = len(board)
        if row_len == 0:
            return False
        col_len = len(board[0])

        self.row_len = row_len
        self.col_len = col_len

        for i in range(row_len):
            for j in range(col_len):
                visited = set([])
                if self.matches(i, j, board, word, visited):
                    return True
        return False
                
            
        
