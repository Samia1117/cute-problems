class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        all_nums = set([i for i in range(n+1)])

        diff = all_nums.difference(set(nums))
        # print(diff)
        return list(diff)[0]
        
