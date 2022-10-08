class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the first and last numbers of the array tell us about 
        # where we need to look: if we need greater than last but less
        # than first, we return -1
        # if we need less than last then look mid and last
        # if we need greater than first, then look first and mid
        # [9, 1, 4, 6, 7] -> 
        # [9, 11, 11, 4, 6, 7] ->
        
        if not nums:
            return []
        low = 0
        high = len(nums)-1
        mid = (low+high)//2
        
        while (high-low)>2: # [6,7,1,2,3,4,5]
            #print("low, mid, high are: ", [low, mid, high])
            if target > nums[high] and target < nums[low]:
                return -1
            if target == nums[mid]:
                return mid
            
            if target<=nums[low]: # [9, 1, 4, 6, 7]
                if target == nums[low]:
                        return low
                if nums[mid] <= nums[low]: # stopped ascending
                    if target>=nums[mid]:
                        low = mid
                    else: # if target < nums[mid]
                        high = mid
                else:   # nums[mid] > nums[low] -> still ascending
                    low = mid
            else:   # target > nums[low]
                if nums[mid] <= nums[low]: # stopped ascending
                    high = mid
                else:   # still ascending
                    if target> nums[mid]:
                        low = mid
                    else:
                        high = mid
            mid = (low+high)//2
            
            
        if nums[low] == target:
            return low
        if nums[mid] == target:
            return mid
        if nums[high] == target:
            return high
        
        return -1
