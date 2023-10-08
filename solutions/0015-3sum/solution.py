class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return []
        
        result = []
        nums.sort()
        n = len(nums)
        
        for l in range(len(nums)-2):
            # for each leftmost number of a triplet, start off with mid just following left and right at the very end, forming an interval [l, m, r]

            # Since nums is sorted, duplicates will be in sequence
            # Set defaults as: l is the first num, m is the next num after l(could be same as l), and r is the rightmost num in the array
            # We already ensure that l will not be duplicate (in next iteration if we find the last l as in l-1, then we ignore it) - so we have to make sure m and r change (for each l) as we move them about to create our interval.
            # to do this, use move m and r around at the same time - adjust the one that needs to increase or decrease until one overshoots the other
            # Make sure once you've found the desired m and l, you choose necessarily other m and l for the next valid interval
            # You can do this by either checking previous m/next r or next m/previous r. The latter is the better choice since initially, previous m is just l. 
            # Now time to code! 
            if (l> 0 and nums[l] == nums[l-1]):
                continue
            
            m, r = l+1, n-1

            while (m < r):

                if (m != l+1 and nums[m] == nums[m-1]):
                    m += 1
                    continue
                if (r != n-1 and nums[r] == nums[r+1]):
                    r -= 1
                    continue

                tripletSum = nums[m] + nums[r] + nums[l]

                if (tripletSum > 0):
                    r -= 1
                elif (tripletSum < 0):
                    m += 1
                else:
                    result.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
        return result



            
        #     if l>0 and nums[l]==nums[l-1]: # if duplicate l, skip it, except the first l
        #         continue
            
        #     m,r = l+1, n
        #     while m<r : # shrink this interval as needed (recall: nums is sorted)
        #         tripletSum = nums[l]+nums[m]+nums[r]

        #         if tripletSum < 0:
        #             m +=1
        #         elif tripletSum > 0:
        #             r -=1
        #         else:
        #             result.append([nums[l], nums[m], nums[r]])
        #             # skip using same left and right for same m
        #             while m<r and nums[m] == nums[m+1]:
        #                 m += 1
        #             while m<r and nums[r] == nums[r-1]:
        #                 r -= 1
        #             r-=1; m+=1
                    
        # return result
        
