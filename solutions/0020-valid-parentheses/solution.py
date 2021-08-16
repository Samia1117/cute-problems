class Solution:
    def isValid(self, s: str) -> bool:
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
        
        
#         opening = s[0]
#         pdict = { "[": "]", "{": "}", "(": ")" }
#         if opening not in pdict:  
#             return False
#         closing = pdict[opening]
        
#         lastOpeningIndex = 0
#         firstClosingIndex = 0
#         try:
#             firstClosingIndex = s.index(closing)
#             lastOpeningIndex = s.rindex(opening,0,firstClosingIndex)
#         except ValueError:
#             return False
        
#         if (firstClosingIndex-lastOpeningIndex)==1:
#             if firstClosingIndex == len(s)-1:
#                 return self.isValid(s[0:lastOpeningIndex])
#             else:
#                 return self.isValid(s[0:lastOpeningIndex]+s[firstClosingIndex+1:])
#         else:
#             if firstClosingIndex == len(s)-1:
#                 return self.isValid(s[lastOpeningIndex+1:firstClosingIndex])
#             else:
#                 return ( self.isValid(s[0:lastOpeningIndex] +s[firstClosingIndex+1:]) and self.isValid(s[lastOpeningIndex+1:firstClosingIndex]) )
        
        
        
        
