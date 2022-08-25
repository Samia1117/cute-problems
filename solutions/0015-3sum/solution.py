class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return []
        
        result = []
        nums.sort()
        
        for m in range(len(nums)-2):
            # for reach mid point, start off with left and right at two very ends, forming an interval around mid
            
            if m>0 and nums[m]==nums[m-1]: # if duplicate m, skip it
                continue
            
            l,r = m+1, len(nums)-1
            while l<r : # shrink this interval as needed (recall: nums is sorted)
                tripletSum = nums[l]+nums[m]+nums[r]

                if tripletSum < 0:
                    l +=1
                elif tripletSum > 0:
                    r -=1
                else:
                    result.append([nums[l], nums[m], nums[r]])
                    # skip using same left and right for same m
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                        
                    r-=1; l+=1
                    
        return result
                    
                
            
#         if nums == []:
#             return []
        
#         sumMap = {}
#         seen = []
#         result = []
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 summ = nums[i] + nums[j]
#                 #print("nums i, j: ", [nums[i], nums[j], i, j])
#                 if summ not in sumMap:
#                     sumMap[summ] = []
#                 sumMap[summ].append([nums[i], nums[j], i, j])
        
#         for k in range(len(nums)):
#             key = -nums[k]
#             if key not in sumMap:
#                 continue
                
#             candidates = sumMap[key]
#             for candidate in candidates:
#                 otherTwoIndices = [candidate[2], candidate[3]]
#                 if k>= candidate[2] or k>=candidate[3]:
#                     continue
#                 #print("k, mid, end: ", [k, candidate[2], candidate[3]])
#                 triplet = [candidate[0], candidate[1], -key]
#                 if set(triplet) in seen:
#                     continue
#                 else:
#                     seen.append(set(triplet))
#                     result.append(triplet)
                    
#         return result
        
#         triplets = []
#         added = []
        
#         for start in range(len(nums)):
#             for mid in range(start+1, len(nums)):
#                 for end in range(mid+1, len(nums)):
#                     if nums[start] + nums[mid] + nums[end] == 0:
#                         setx = set()
#                         setx.update([nums[start], nums[mid], nums[end]])
#                         seen = False
#                         for i in range(len(added)):
#                             if added[i] == setx:
#                                 seen = True
#                                 break
#                         if not seen:
#                             triplets.append([nums[start], nums[mid], nums[end]])
#                             added.append(setx)
                        
#         return triplets
                        
        
