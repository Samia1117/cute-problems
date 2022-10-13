class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in hashMap:
                return [hashMap[num], i]
            want = target-num
            hashMap[want] = i
        
        
            
        
