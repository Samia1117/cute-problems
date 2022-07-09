class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        else:
            mid = len(nums)//2
            low = 0
            high = len(nums) - 1
            while low != mid: # we want to narrow in
                # print("mid, low, high are now: ", str(mid)+ " "+str(low)+" "+str(high) )
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        low = mid
                    else:
                        high = mid
                        
                    mid = (high+low)//2
            
            if nums[high] == target:
                return high
            if nums[mid] == target:
                return mid
            return -1
                    
                        
