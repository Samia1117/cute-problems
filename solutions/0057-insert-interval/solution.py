class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left = []
        right = []
        toMerge = []
        
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:    # starts earlier, ends earlier
                left.append(interval)
            elif interval[0] > newInterval[0] and interval[0] > newInterval[1]: # starts later than new Interval's start and new Interval's end
                right.append(interval)
            else:
                toMerge.append(interval)
        
        toMerge.append(newInterval)
        minStart = min([toMerge[i][0] for i in range(len(toMerge))])
        maxEnd = max([toMerge[i][1] for i in range(len(toMerge))])
        
        overlapInterval = [minStart, maxEnd]
        left.append(overlapInterval)
        
        return left + right
            
                
        
        
