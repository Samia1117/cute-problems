class Solution {

    public String minWindow(String s, String t) {

        // Map char: frequency of char
        HashMap<Character, Integer> tmap = new HashMap<>();
        for (char c: t.toCharArray()) {
            int frequency = tmap.getOrDefault(c, 0);
            tmap.put(c, frequency + 1);
        }

        // System.out.println("tmap = " + tmap);
        int right = 0; int left = 0;
        HashMap<Character, Integer> smap = new HashMap<>();
        int desiredCount = tmap.size();
        // System.out.println("Desired count = " + desiredCount);

        int currCount = 0;
        String minWindow = "";
        int minWindowSize = Integer.MAX_VALUE;
// ADOB
// ECOD
// EBAN
// C
        while (right < s.length()) {
            Character currChar = s.charAt(right);
            int frequency = smap.getOrDefault(currChar, 0) + 1;
            smap.put(currChar, frequency); // this map is keeping track of current frequency
            // System.out.println("smap = " + smap);
            // System.out.printf("left, right = %d, %d\n", left, right);

            if (tmap.containsKey(currChar) && tmap.get(currChar) == frequency) {
                // increment when not only the char is present but present at the right frequency
                currCount++;
            }

            if (currCount == desiredCount) {
                // we have all the desired letters, at the right frequency
                while (left <= right && currCount == desiredCount) {
                    // squeeze window to the right as long as we don't remove a char needed to make 't'
                    int windowSize = right-left+1; // 3 - 0 + 1 = 4
                    if (windowSize < minWindowSize) {
                        minWindowSize = windowSize;
                        minWindow = s.substring(left, right + 1);
                    }
                    Character key = s.charAt(left);
                    smap.put(key, smap.get(key) - 1);
                    if (tmap.containsKey(key) && smap.get(key) < tmap.get(key)) {
                        currCount--;
                    } 
                    left++; // Keep advancing the left ptr
                }
            }
            
            right++;
        }
        return minWindow;
    }
}
