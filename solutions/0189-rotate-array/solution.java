class Solution {
    public void rotate(int[] nums, int k) {

        int n = nums.length;
        if (k >= n) {
            k = k % n;
        }
        if (k == 0) {
            return;
        }

        int l = 0;
        int r = n-k;

        List<Integer> lastKElts = new ArrayList<>();
        List<Integer> firstNMinusKElts = new ArrayList<>();
        // System.out.printf("r, n, k = %d, %d, %d\n", r, n, k);

        while (r < n) { // this loop should run for k times only
            lastKElts.add(nums[r]);
            r++;
        }

        // System.out.printf("lastKElts = %s\n",lastKElts);

        while (l < n-k) {
            firstNMinusKElts.add(nums[l]);
            l++;
        }
        // System.out.printf("firstNMinusKElts = %s\n", firstNMinusKElts);

        // Now replace values in nums array in place

        for (int i = 0; i < n; i++) {
            // System.out.printf("i = %d, i-(n-k)= %d\n", i, i - (n - k));
            if (i < k) {
                nums[i] = lastKElts.get(i);
            } else {
                nums[i] = firstNMinusKElts.get(i - k);
            }
            // System.out.printf("nums[i] = %d\n", nums[i]);
        }
        // System.out.printf("Nums = %s\n", nums);
    }
}
