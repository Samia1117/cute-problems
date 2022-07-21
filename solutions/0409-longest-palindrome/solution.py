class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        charDict = {}
        
        for ch in s:
            if ch not in charDict:
                charDict[ch] = 0
            charDict[ch] +=1
            
        length = 0
        
        for k,v in charDict.items():
            length += (v//2) * 2
            charDict[k] -= 2*(v//2)
        
        for val in charDict.values(): 
            if val>0:
                return length +1
            
        return length
        
