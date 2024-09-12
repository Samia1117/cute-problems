class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = []
        d = {} # key = num, value = index of num
        idx = 0
        for num in nums:
            if num in d:
                if num+num == target:
                    return [d[num], idx]
            elif num not in d:
                d[num] = idx
            targetNum = target - num
            if targetNum == num:
                pass
            elif targetNum in d:
                # found !
                ret = [d[num], d[targetNum]]
                return ret
            idx += 1
        
