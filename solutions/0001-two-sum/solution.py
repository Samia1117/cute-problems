class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        i = 0
        for num in nums:
            keyNeeded = target - num
            # print("key needed is: ", keyNeeded)
            if keyNeeded in d:
                return [d[keyNeeded], i]
            d[num] = i
            # print("d is: ", d)
            i +=1
            
        return []
