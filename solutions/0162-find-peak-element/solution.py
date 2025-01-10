class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        
        low, high = 0, n-1
        while low < high:
            mid = (low + high)//2
            # print("low, high, mid = ", [low, high, mid])
            if nums[mid] <= nums[mid+1]:
                # ascending sequence
                low = mid + 1
            else:
                # strictly descending sequence
                high = mid
        return low
        


        
