
import java.lang.Math;

class Solution {

    Pair<Integer, Integer> robEven(int[] nums) {
        int pattern1 = 0; // uses first house
        int pattern2 = 0; // uses last house
        int numHouses = nums.length;
        for (int i=0; i < numHouses; i++) {
            if (i%2 == 0) { // even
                pattern1 += nums[i];
            } else { // odd
                pattern2 += nums[i];
            }
        }
        return new Pair<Integer, Integer>(pattern1, pattern2);
    }
    public int rob(int[] nums) {
        
        int numHouses = nums.length;
        if (numHouses == 1) {
            return nums[0];
        }
        if (numHouses == 0) {
            return 0;
        }

        // Dynamic programming
        // let dp[i] = maximum profit we can gain if number of houses stopped at nums[i]
        //  max (without using nums[i], with using nums[i])

        int[] dp = new int[numHouses];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < numHouses - 1; i++) {
            dp[i] = Math.max(
                dp[i-2] + nums[i], // use this house
                dp[i-1] // don't use this house
            );
        }

        int[] dp2 = new int[numHouses];
        dp2[numHouses - 1] = nums[numHouses - 1];
        dp2[numHouses - 2] = Math.max(nums[numHouses - 1], nums[numHouses - 2]);
        for (int i = numHouses - 3; i > 0; i--) {
            dp2[i] = Math.max(
                dp2[i+2] + nums[i], // use this house
                dp2[i+1] // don't use this house
            );
        }

        return Math.max(dp[numHouses - 2], dp2[1]);


    }
}
