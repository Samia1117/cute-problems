class Solution {
    private List<String> wordDict;
    private String s;
    private int[] dp;

    public boolean checkWordBreak(int i) {
        if (i < 0) {
            return true;
        }

        if (dp[i] != -1) {
            // already visited
            return dp[i] == 1;
        }

        for (String word: wordDict) {
            int newWordStart = i - word.length() + 1; 
            // e.g. i = 10, wordLength = 6, so word.length() is 4. Check that the word:
            // s[5] + s[6] + s[7] + s[8] + s[9] + s[10] is a word AND that dp[4/word.length()] is true
            if (newWordStart < 0) {
                continue;
            } 
            if (s.substring(i-word.length() + 1, i+1).equals(word) && checkWordBreak(i-word.length())) {
                dp[i] = 1;
                return true;
            }
        }

        dp[i] = 0;
        return false;
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        if (s.length() == 0) {
            return true;
        }

        // Let dp[i] = if it is possible to wordBreak ending at s[i]
        // Return dp[s.length() - 1]

        // Base case: dp[i<0] = true
        // dp[i] (i > = 0) := if 1) there exists an index j < i, such that s.substring(j, i+1) is a word in the dictionary of words
        // 2) dp[j-1] is also true (it is possible to wordBreak ending at s[j-1])

        boolean[] dp = new boolean[s.length()];
        HashSet<String> words = new HashSet<>(wordDict);
        for (int i=0; i<s.length(); i++) {
            for (String word: words) {                
                // System.out.printf("Word = %s\n", word);
                int endIndex = i - word.length(); // 10 - 6
                int startIndex = endIndex + 1;

                if (startIndex < 0) {
                    continue;
                } else {
                    if (startIndex == 0 || dp[endIndex]) { // endIndex must be >= 0 here
                        // possible to wordBreak with s[:i]
                        String possibleWord = s.substring(startIndex, i+1);
                        // System.out.printf("Possible word = %s\n", possibleWord);
                        if (words.contains(possibleWord)) {
                            dp[i] = true;
                            // System.out.printf("DP was filled with a 1 at %d\n", i);
                            // System.out.println(Arrays.toString(dp));
                            continue;
                        }
                    }
                }
            }
        }

        return dp[s.length() - 1];


        // this.s = s;
        // this.wordDict = wordDict;
        // this.dp = new int[s.length()];
        // Arrays.fill(this.dp, -1);
        // return checkWordBreak(s.length() - 1);

        /** 
        * Good approach but fails runtime requirement

        LinkedList<Integer> deque = new LinkedList();
        deque.addLast(0);
        HashSet<String> words = new HashSet<>(wordDict);
        boolean[] seen = new boolean[s.length()+1];
        seen[0] = true;

        while (!deque.isEmpty()) {
            int start = deque.pollLast();
            if (start == s.length()) { 
                // we have reached a starting point that came right after the close of a word and
                // this starting point happens to be the end - i.e. we 'word hopped' our way out of 
                // the initial word 's'
                return true;
            }
            for (int end = start + 1; end <= s.length(); end++) {
                String possibleWord = s.substring(start, end); 
                if (words.contains(possibleWord)) {
                    if (!seen[end]) {
                        deque.addLast(end); // another possible start for a word
                    }
                }
            }
        }
        return false;
        */
    }
}
