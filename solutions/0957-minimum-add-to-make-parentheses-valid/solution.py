from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        if not s:
            return 0

        st = deque()
        count = 0
        
        for ch in s:
            if ch == '(':
                st.append(ch)
            elif ch == ')':
                if not st:
                    count += 1 
                else:
                    st.pop()
        count += len(st)

        return count
        
