class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> numToCount = new HashMap<Integer, Integer>();

        int i = 0;
        while (i < nums.length) {
            if (!numToCount.containsKey(nums[i])) {
                numToCount.put(nums[i], 0);
            }
            numToCount.put(nums[i], numToCount.get(nums[i]) + 1);
            if (numToCount.get(nums[i]) > 1) {
                return true;
            }
            i++;
        }
        return false;
    }
}
