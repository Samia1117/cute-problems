class Solution:
    
    def make_new_combs(self, x, ylist):
        # 1; [2, 3, 4]
        
        ret = []
        n = len(ylist)
        # [2, 3, 4] -> [1], [1, 2], [1, 2, 3], [1, 2, 3, 4]
        # -> [2], [2, 1], [2, 1, 3], [2, 1, 3, 4]
        for i in range(n+1):
            tempylist = ylist.copy()
            comb = []
            for j in range(n+1):
                if j ==i:
                    comb.append(x)
                else:
                    comb.append(tempylist[0])
                    tempylist = tempylist[1:]
            ret.append(comb)
        return ret
                    
                
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0 or len(nums)==1:
            return [nums]

        n = len(nums)
        
        # ylist = [2, 3, 4]
        # ret = self.make_new_combs(1, ylist)
        # print("make new combs returned: ", ret)
        
        ylists = self.permute(nums[1:])  # list of lists
        x = nums[0]
        
        all_combs = []
        
        for ylist in ylists:
            ret = self.make_new_combs(x, ylist)
            #print("found new combination: ", ret)
            all_combs += ret
                
        return all_combs
    
    
    
    
    
    
    
    
    
