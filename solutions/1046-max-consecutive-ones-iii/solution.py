class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        max_seq_len = 0
        
        left, right = 0, 0
        num_zeroes = 0 

        # print(f'k = {k}, n={n}')
        while right < n:
            if nums[right] == 0:
                num_zeroes += 1
            # print(f'longest sequence in previous run = {max_seq_len}')
            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1            
            max_seq_len = max(max_seq_len, right-left+1)
            right += 1            
        
        return max_seq_len

        
