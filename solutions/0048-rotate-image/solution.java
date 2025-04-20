class Solution {

    void transpose(int[][] matrix) {
        if (matrix.length <= 1) {
            return;
        }
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            // iterate the upper triangular section
            // swap the diagonally opposite entries 
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        System.out.println("After transpose: " + Arrays.deepToString(matrix));
        return;
    }

    void flipVertical(int[][] matrix) {
        if (matrix.length <= 1) {
            return;
        }
        int n = matrix.length;
        int mid = (int) Math.floor(n / 2);

        for (int i = 0; i < mid; i++) {
            // i indicates top row, n-i indicates bottom row
            int[] tempTopRow = matrix[i];
            matrix[i] = matrix[n-i-1];
            matrix[n-i-1] = tempTopRow;
            // if i == n-i-1 (when odd), this operation will have no effect
        }
        System.out.println("After flipping vertically: " + Arrays.deepToString(matrix));
    }

    public void rotate(int[][] matrix) {
        // (1, 2, 3) -> (3, 6, 9); (0,0) -> (0,2), (0,1) -> (1,2), (0,2) -> (2,2)
        // (4, 5, 6) -> (2, 5, 8); (1, 0) -> (0,0)
        // (7, 8, 9) -> (1, 4, 7)

        // (1, 2, 3, 4) -> (4, 8, 12, 16)
        // (5, 6, 7, 8) -> (3, 7, 11, 15)
        // ...

        // Pattern: for row,col in matrix, 
        // matrix[row][col] = (n - row) + (n * col) 

        flipVertical(matrix);
        transpose(matrix);
    }
}
