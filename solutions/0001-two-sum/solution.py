class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        twoIndices = []
        list_len = len(nums)
        for i in range(list_len):
            for j in range(i+1, list_len):
                if nums[i] + nums[j] == target:
                    twoIndices.append(i)
                    twoIndices.append(j)
                    return twoIndices
        
