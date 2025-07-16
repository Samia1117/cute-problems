class Solution:
    def findMin(self, nums: List[int]) -> int:
        # basically, need values to 'wrap around' when shifting no longer applicable
        # should we find the rotation factor?
        # typically, a[0] will be min. If not, 

        # so if relationship is 'increasing', look to the right
        # find where relationship goes from 'increasing' to decreasing. Return lower valued elt

        # one caveat, if a[0] <= a[1], return a[0

        if len(nums) == 1:
            return nums[0]
        
        if nums[0] <= nums[-1]: # not rotated. Note: unique elements
            return nums[0]

        max_right_arr = nums[-1]

        low, high = 0, len(nums) - 1

        while low < high:
            mid = (high + low) // 2
            # print(f'low, mid, high = {low, mid, high}')

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
            
            if low == mid:
                if nums[low] < nums[high]:
                    return nums[low]
        
        return -1
        
        

