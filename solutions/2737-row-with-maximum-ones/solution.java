class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        
        int maxSum = -1 * Integer.MAX_VALUE;
        int maxIdx = 0;
        for (int i = 0; i < mat.length; i++) {
            int sum = Arrays.stream(mat[i]).sum();
            if (sum > maxSum) {
                maxSum = sum;
                maxIdx = i;
            }
        }
        return new int[] {maxIdx, maxSum}; 
    }
}
