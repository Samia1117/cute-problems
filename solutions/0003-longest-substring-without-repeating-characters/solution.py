class Solution:
            
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
        start = 0
        maxLength = 0
        usedChars = {}  # keep track of where this char was last seen
        
        for i in range(len(s)):
            if s[i] in usedChars and start <= usedChars[s[i]]:
                start = usedChars[s[i]] + 1 # start at a new place; max seen for this letter
            else:
                maxLength = max(maxLength, i-start+1)
            
            usedChars[s[i]] = i
        return maxLength
            
# It was a good DP attempt ...
#       dp = [[0 for _ in range(len(s))] for k in range(len(s))]
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if i==j:
#                     dp[i][j] = 1
#                 else:
#                     if s[j] in set(s[i:j]):
#                         break
#                     else:
#                         dp[i][j] = dp[i][j-1] + 1   
#         lastCol = [max(dp[i]) for i in range(len(s))]
#         return max(lastCol)
        
        
        
        
        
        
        
