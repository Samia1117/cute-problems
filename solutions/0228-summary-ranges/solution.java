import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {

        List<String> ranges = new ArrayList<>();

        int n = nums.length;

        if (n == 0) {
            return ranges;
        }

        if (n == 1) {
            return List.of(String.valueOf(nums[0]));
        }

        int rangeStart = nums[0];
        int rangeEnd = nums[0];

        for (int i = 1; i < n; i++) {
            // System.out.println("rangeStart = " + rangeStart + " rangeEnd " + rangeEnd);
            int nextNum = nums[i];
            // System.out.println("nextNum = " + nextNum);
            double diff = (double) nextNum - (double) rangeEnd;
            if (diff  > 1) {
                // create a new range
                if (rangeStart == rangeEnd) {
                    ranges.add(String.valueOf(rangeStart));
                } else {
                    String range = String.valueOf(rangeStart) + "->" + String.valueOf(rangeEnd);
                    ranges.add(range);
                }

                rangeStart = nextNum;
                rangeEnd = nextNum;
                if (i == n-1 ) {
                    ranges.add(String.valueOf(nextNum));
                }
            } else {
                rangeEnd = nextNum;
                if (i == n-1) {
                    String range = String.valueOf(rangeStart) + "->" + String.valueOf(rangeEnd);
                    ranges.add(range); 
                }
            }
        }
        
        System.out.println("Ranges = " + ranges);
        return ranges;
    }
}
