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
            #if keyNeeded in d:
                #return [d[keyNeeded], i]
            #d[num] = i
            d[keyNeeded] = [i] # i is the index of one of the numbers
            i +=1
        
        i = 0
        for num in nums:
            if num in d:
                if i!=d[num][0]:
                    #print("i, d[num] ", [i, d[num][0]])
                    d[num].append(i)
                    return d[num]
            i +=1
        return []
