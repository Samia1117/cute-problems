class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # At any given point, if we meet the following condition, we have a valid contiguous array with an equal # of 0 and 1
        # if sum(arr[l:r]) == r-l + 1/2
        # It's a sliding window problem -> if you slide to one more place you lose the equal # of 0 and 1 condition, so increase left until sum becomes 0 again

        n = len(nums)
        if n <= 1:
            return 0

        max_arr_len = 0 
        hmap = {0:-1} 
        curr_sum = 0


        for i in range(n):
            curr_sum += -1 if nums[i] == 0 else nums[i]
            if curr_sum not in hmap:
                hmap[curr_sum] = i
            else:
                max_arr_len = max(max_arr_len, i-hmap[curr_sum])
        
        return max_arr_len
        
