class Solution {

    private static int maxRow;
    private static int maxCol;

    private static boolean isInBounds(int row, int col) {
        if (row < 0 || col < 0) {
            return false;
        }
        if (row >= maxRow || col >= maxCol) {
            return false;
        }
        return true;
    }
    /**
        Modifies the grid in place. Start from grid[i][j]
     */
    private void bfs(int i, int j, char[][] grid) {
        if (grid[i][j] == '1') {
            grid[i][j] = 'X';
        } else {
            return;
        }

        // neighbor down
        if (isInBounds(i+1, j)) {
            bfs(i+1, j, grid);
        }

        // neighbor up
        if (isInBounds(i-1, j)) {
            bfs(i-1, j, grid);
        }

        // neighbor to right
        if (isInBounds(i, j+1)) {
            bfs(i, j+1, grid);
        }

        // neighbor to left
        if (isInBounds(i, j-1)) {
            bfs(i, j-1, grid);
        }
    }

    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }

        int rows = grid.length;
        int columns = grid[0].length;
        this.maxRow = rows;
        this.maxCol = columns;

        int numIslands = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid[i][j] == '1') {
                    bfs(i, j, grid);
                    numIslands++;
                }
            }
        }

        return numIslands;
    }
}
