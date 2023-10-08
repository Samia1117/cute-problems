class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        else:
            # currentSum = 0
            # keep adding to current sum as long as the sum stays > 0. 
            # If sum must be <= 0, then we should simply choose the element with greatest value
            # If ever sum goes beyond zero by adding the next element, then choose a new left pointer
            # At the end we should compare whether maxElt or maxSum is greater
            maxSum = -10000
            maxElt = -10000
            currentSum = 0

            for i in range(len(nums)):
                if currentSum + nums[i] < 0:
                    if maxSum < currentSum:
                        maxSum = currentSum
                    currentSum = 0
                else:
                    currentSum += nums[i]
                
                if maxSum < currentSum:
                    maxSum = currentSum
                if nums[i] > maxElt:
                    maxElt = nums[i]
            
            if maxElt < 0 or maxElt > maxSum:
                maxSum = maxElt 
            
            return maxSum
                
