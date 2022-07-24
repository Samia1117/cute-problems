class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        numsDict = {}
                
        for num in nums:
            if num not in numsDict:
                numsDict[num] = 0
            else:
                return True
            
        return False
        
