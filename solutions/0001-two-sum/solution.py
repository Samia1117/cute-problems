class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        two_dexes = []
        list_len = len(nums)
        for i in range(0, list_len):
            for j in range(i+1, list_len):
                if nums[i] + nums[j] == target:
                    two_dexes.append(i)
                    two_dexes.append(j)
                    return two_dexes
        return []
        
        
