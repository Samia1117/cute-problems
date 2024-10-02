class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        # s = set()

        i = 0
        for num in nums:
            complement = target - num
            if complement in d:
                return [d[complement], i] 
            d[num] = i
            i += 1

        return []
