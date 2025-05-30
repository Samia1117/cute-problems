class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, n):
            
            # Note, nums[i] + current_sum is going to be greater than nums[i] only if current_sum is positive. 
            # If current_sum is not positive, it won't help to use it. We may as well start from nums[i]
            current_sum = max(nums[i] + current_sum, nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

        
