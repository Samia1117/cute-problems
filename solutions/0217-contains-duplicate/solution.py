class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) != len(set(nums)):
            return True
        return False

        # d = {}

        # for num in nums:

        #     if num in d:
        #         return True
        #     else:
        #         d[num] = 0
        
        # return False
        
