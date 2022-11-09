class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n= len(nums)
        if n ==0 or n==1:
            return n
        
        prev, r = 0,1
        while r<n:
            while nums[prev] == nums[r] and r<n:
                #print("prev, r: ", [prev, r])
                r +=1
                if r==n:
                    return prev+1
            prev +=1
            nums[prev] =nums[r]
            r +=1
            #print("after swap: ", nums)
            #print("r, prev were: {}, {}".format(r, prev))
        return prev+1
            
