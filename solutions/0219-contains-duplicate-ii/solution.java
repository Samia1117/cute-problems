class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        /** Return true if there exists an instance of repeated numbers 
        in 'close proximity' (within 'k') of each other  */

        if (nums.length <= 1) {
            return false;
        }

        Map<Integer, Integer> numToCountMap = new HashMap<>();

        int index = 0;
        for (int num: nums) {
            if (!numToCountMap.containsKey(num)) {
                numToCountMap.put(num, index);
            }

            int prevIdx = numToCountMap.get(num);
            int currIdx = index;

            if (currIdx != prevIdx && (currIdx - prevIdx <= k)) {
                return true;
            }

            numToCountMap.put(num, index);
            // numToCountMap.forEach((key, value) -> System.out.println("key: " + key + ", value: " + value) );

            index += 1;
        }
        
        return false;
    }
}
