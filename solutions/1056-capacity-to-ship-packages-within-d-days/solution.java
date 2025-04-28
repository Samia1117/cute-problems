class Solution {

    private int binSearchNumDaysRequired(int min, int max, int[] weights, int days) {

        System.out.printf("Min %s, Max %s = \n", min, max);
        if (min == max) {
            return min;
        }
        if ( (min - max) == 1) {
            if (getNumDaysRequired(min, weights) > days) {
                return max;
            } else {
                return min;
            }
        }
        int mid = (min+max) / 2;
        if (getNumDaysRequired(mid, weights) <= days) {
            return binSearchNumDaysRequired(min, mid, weights, days);
        } else {
            return binSearchNumDaysRequired(mid + 1, max, weights, days);
        }
    }
    private int getNumDaysRequired(int minCapacity, int[] weights) {
        int days = 0;
        int n = weights.length;

        int currentBatchSize = 0;
        int i = 0;
        while (i < n) {
            while (i < n && (currentBatchSize + weights[i] <= minCapacity)) {
                currentBatchSize += weights[i];
                i ++;
            }
            days++;
            // System.out.println("Num packages taken care of = " + i);
            // System.out.println("Days = " + days);
            currentBatchSize = 0;
        }
        return days;
    }
    public int shipWithinDays(int[] weights, int days) {

        int minCapacity = Arrays.stream(weights).max().getAsInt();
        int maxCapacity = Arrays.stream(weights).sum();

        return binSearchNumDaysRequired(minCapacity, maxCapacity, weights, days);

        // while (true) {
        //     int daysWithCurrentMinCap = getNumDaysRequired(minCapacity, weights);
        //     System.out.println("Min capacity = " + minCapacity);
        //     System.out.println("Days required = " + daysWithCurrentMinCap);
        //     if (daysWithCurrentMinCap > days) {
        //         minCapacity += 1;
        //     } else {
        //         return minCapacity;
        //     }
        // }
    }
}
