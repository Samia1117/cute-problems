class Solution {

    class PairComparator implements Comparator<Pair<Integer, Integer>> {

        @Override
        public int compare(Pair<Integer, Integer> p1, Pair<Integer, Integer> p2) {
            return p2.getValue() - p1.getValue();   // compare based on second element
        }
    }
    public int[] topKFrequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> numToCountMap = new HashMap<>();

        for (int num: nums) {
            if (!numToCountMap.containsKey(num)) {
                numToCountMap.put(num, 0);
            }
            numToCountMap.put(num, numToCountMap.get(num) + 1);  // increment how many times 'num' has been seen
        }

        // System.out.println("numToCountMap = " + numToCountMap);

        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> a.getValue() - b.getValue());
        // PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        List<Pair<Integer, Integer>> pairs = numToCountMap.entrySet().stream()
                                    .map(e -> new Pair<Integer, Integer> (e.getKey(), e.getValue()) )
                                    .collect(Collectors.toList());

        for (Pair<Integer, Integer> pair: pairs) {
            pq.add(pair);
            if (pq.size() > k) {
                while (pq.size() > k) {
                    pq.poll();
                }
            }
        }

        // System.out.println("PQ = " + pq);

        int[] ret = new int[k];
        for (int i=0; i<k; i++) {
            ret[i] = pq.poll().getKey();
        }

        return ret;

        // for (Entry<Integer, Integer> kv: )
    }
}
