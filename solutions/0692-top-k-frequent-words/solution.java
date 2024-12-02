class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        
        int n = words.length;

        if (n <= 1) {
            return new ArrayList<String>(Arrays.asList(words));
        }

        // 1. Build a frequency dictionary
        HashMap<String, Integer> wordToCount = new HashMap<>();
        for (String word: words) {
            if (!wordToCount.containsKey(word)) {
                wordToCount.put(word, 0);
            }
            wordToCount.put(word, wordToCount.get(word) + 1);
        }

        List<String> topKWords = new ArrayList<>();
        // System.out.println("wordToCount map = " + wordToCount);

        // if both words are equally frequent, then break ties based on lexicographical order
        PriorityQueue<Pair<String, Integer>> pq = new PriorityQueue<>((a, b) -> a.getValue() == b.getValue() ? b.getKey().compareTo(a.getKey()) : a.getValue() - b.getValue());

        for (Map.Entry<String, Integer> entry: wordToCount.entrySet()) {
            Pair<String, Integer> pair = new Pair<>(entry.getKey(), entry.getValue());
            pq.add(pair);
            if (pq.size() > k) {
                // remove the 'top' element - i.e. the one with lowest frequency or the alphabetically GREATER (if two or more words have the same frequency)
                pq.poll();
            }
        }

        // We are left with priority queue  of elements with highest frequency (or the alphabetically SMALLER (if two or more words have the same frequency))
        System.out.println("PQ = " + pq);

        // 3. Format the final result
        int i = 0;
        while (i < k) {
            // recall that polling will still deque elements in the 'reverse' or wrong order. But this is easy to fix by using Collections.reverse()
            Pair<String, Integer> pair2 = pq.poll();    
            topKWords.add(pair2.getKey());
            i ++;
        }
        Collections.reverse(topKWords);
        return topKWords;
    }
}
