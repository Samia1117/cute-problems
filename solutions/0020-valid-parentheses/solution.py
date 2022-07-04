class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        if len(s)==1:
            return False
        
        st = deque()
        opening = ["[", "{", "("]
        closing = ["]", "}", ")"]
        pdict = { "[": "]", "{": "}", "(": ")" }
        
        while s:
            #print("st: ", st)
            if s[0] in opening:
                st.append(s[0])
                s = s[1:]
            else:
                if not st:
                    return False
                if st[-1] not in pdict:
                    return False
                if s[0] == pdict[st[-1]]:
                    st.pop()
                    s = s[1:]
                else:
                    return False
                
        if st:
            return False
        return True
                
                
                
                
                
                
                
