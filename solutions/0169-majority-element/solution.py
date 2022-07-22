class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return None
        
        majorNum = nums[0]
        count = 0
        for i in range(len(nums)):
            
            if nums[i] == majorNum:
                count +=1
            elif count == 0:
                majorNum = nums[i]
            else:
                count -=1  # other element
        
        return majorNum
        
