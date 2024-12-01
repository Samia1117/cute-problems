class Solution {
    public int[] dailyTemperatures(int[] temperatures) {

        int n = temperatures.length;
        if (n <= 1) {
            return new int[n];
        }
        
        int[] answer = new int[n];
        Stack stack = new Stack<Integer>();

        for (int i = 0; i < n; i++) {
            // while the current temperature overcomes the temperature of a (series of) cold day(s) in stack
            while (!stack.empty() && temperatures[i] > temperatures[(int) stack.peek()]) {
                // for this index, found another index i where the temperature is higher
                int index = (int) stack.pop();
                answer[index] = i - index;    
            }
            // push the day that awaits a warmer temperature
            // will be popped when a warmer day is seen, and answer will be stored in the stack
            stack.push(i);
        }

        return answer;
    }
}
