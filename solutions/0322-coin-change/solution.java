class Solution {

    // private int coinChange(int[] coins, int remainingAmt, int[] count)
    public int coinChange(int[] coins, int amount) {

        if (amount <= 0) {
            return 0;
        }
        
        int[] minCoins = new int[amount+1];
        Arrays.fill(minCoins, amount+1);
        // base case: amount = 0, min coins = 0
        minCoins[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    minCoins[i] = Math.min(minCoins[i], minCoins[i - coins[j]] + 1);
                }
            }
        }

        return minCoins[amount] > amount ? -1 : minCoins[amount];
    }
}
