class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        LinkedList<Integer> deque = new LinkedList<Integer>();
        deque.addFirst(0);

        Set<String> words = new HashSet<String>(wordDict);
        boolean[] seen = new boolean[s.length() + 1];

        while (!deque.isEmpty()) {
            int start = deque.pollLast();
            if (start == s.length()) {
                return true;
            }

            for (int end = start + 1; end <= s.length(); end ++) {
                if (seen[end]) {
                    continue;
                }
                if (words.contains(s.substring(start, end))) {
                    deque.addLast(end);
                    seen[end] = true;
                }
            }
        }

        return false;



    }
}
