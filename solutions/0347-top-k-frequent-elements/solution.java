class Solution {

    class EntryComparator implements Comparator<Map.Entry<Integer, Integer>> {

        @Override
        public int compare(Map.Entry<Integer, Integer> p1, Map.Entry<Integer, Integer> p2) {
            return p1.getValue() - p2.getValue(); // compare frequency 
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> numToCountMap = new HashMap<>();
        if (k <= 0) {
            return nums;
        }

        for (int num: nums) {
            if (!numToCountMap.containsKey(num)) {
                numToCountMap.put(num, 0);
            }
            // increment the frequency of num everytime it is seen
            numToCountMap.put(num, numToCountMap.get(num) + 1);  
        }

        // PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(new EntryComparator());

        // Add the top k elements to the priority queue. Remove whenever numElts exceeds k
        for (Map.Entry<Integer, Integer> entry: numToCountMap.entrySet()) {
            pq.add(entry);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[] toRet = new int[k];
        int i = 0;
        while (!pq.isEmpty()) {
            toRet[i] = pq.poll().getKey();
            i += 1;
        }
        return toRet;
    }
}
