class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = list(magazine)
        
        charDict = {}
        
        for ch in chars:
            if ch not in charDict:
                charDict[ch] = 0
            charDict[ch] +=1
        
        requiredChars = list(ransomNote)
        
        for reqChar in requiredChars:
            if reqChar not in charDict:
                return False
            if charDict[reqChar] <=0:
                return False
            charDict[reqChar] -=1
            
        return True
            
            
            
            
        
