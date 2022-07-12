class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        i = 0
        maxElt = -10000
        maxSum = -10000
        currentSum = 0
        while i < len(nums):
            elt = nums[i]
            if elt > maxElt:
                maxElt = elt
            if currentSum + elt < 0:
                i +=1
                currentSum = 0
            else:
                currentSum += elt
                if currentSum > maxSum:
                    maxSum = currentSum
                i +=1
            #print("current sum: ", currentSum)

        if maxSum == -10000:
            return maxElt
        return maxSum
#         maxSum = -10000
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 currentSum = sum(nums[i:j+1])
#                 if currentSum > maxSum:
#                     maxSum = currentSum
        
#         return maxSum            
                
#         return self.helperMSA(nums, False)
    def helperMSA(self, nums, includeLast):
        
        if len(nums) == 0:
            return 0
        if includeLast:
            if len(nums) == 1:
                return nums[0]
            else:
                return nums[0] + self.helperMSA(nums[1:], True)
        
        else:
            return max (
            nums[0] + self.helperMSA(nums[1:], True),
            self.helperMSA(nums[1:], False)
            )
        
