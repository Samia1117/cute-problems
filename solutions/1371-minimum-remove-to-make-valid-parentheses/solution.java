class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> stack = new Stack<>();
        HashSet<Integer> idxTracker = new HashSet<>();

        for (int i = 0; i< s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                stack.push(i);  // keep track of indices of '('. If not popped by else, then need to pop manually
            } else if (ch == ')') {
                if (stack.empty()) {
                    // ')' should be removed from word
                    idxTracker.add(i);
                } else {
                    stack.pop();
                }
            }
        }

        while (!stack.empty()) {
            idxTracker.add(stack.pop());
        }

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<s.length(); i++) {
            if (!idxTracker.contains(i)) {
                sb.append(s.charAt(i));
            }
        }


        return sb.toString();
    }
}
