import sys 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set, 's' of nums. Loop through each num in s ->  O(n)
        # identify the 'lowest', 'l', of a sequence. If l-1 does not exist, 
        # keep incrementing by l + seq.length., starting with seq.length. = 1
        # so we will do O(n) lookups during this incrementation step
        # But we will only look up a number at most twice (once while looping, once while checking if it is in 's', as part of some other sequence)
        # So runtime = O(2n) = O(n)

        if nums == None or len(nums) == 0:
            return 0

        # d = {}
        # minKey = sys.maxsize
        lcs = 0

        s = set(nums)

        for num in s:
            if num - 1 not in s: # we can 'start' a seq. at this number
                length = 1
                while num + length in s:
                    length += 1
                lcs = max(lcs, length)

        return lcs


        
