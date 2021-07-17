class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        runsum = 0
        rlist = []
        for i in range(len(nums)):
            runsum += nums[i]
            rlist.append(runsum)
        return rlist
