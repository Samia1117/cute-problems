import numpy as np
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        r = len(height) -1
        l = 0
        
        while(l<r):
            
            area = (r-l)* min(height[l],height[r])
            maxarea = max(area, maxarea)
            
            if height[r]>=height[l]: # this is the best that left could do
                l +=1
            else:
                r -=1
        
        return maxarea
            
        
