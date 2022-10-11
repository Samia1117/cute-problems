class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        if n==0 or n==1:
            return intervals
        
        ret = []
        newInterval = intervals[0]
        ret.append(newInterval)
        
        for interval in intervals:
            if interval[0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newInterval = interval
                ret.append(newInterval)
        
        return ret
    
            
