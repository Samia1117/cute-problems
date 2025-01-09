class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)

        if n == 0 or n == 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x:x[1])
        intervals = sorted(intervals, key=lambda x:x[0])
        merged_intervals = []

        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]

            if curr_interval[0] <= prev_interval[1]: 
                # prev interval ends after curr intervals starts
                prev_interval[1] = max(curr_interval[1], prev_interval[1])
            else:
                merged_intervals.append(prev_interval)
                prev_interval = curr_interval
        
        merged_intervals.append(prev_interval)
        return merged_intervals


'''
        i = 0
        while i < n:
            interval_to_merge = intervals[i]
            # while endTime of this interval exceeds the startTime of next interval, don't add it to final list; keep merging
            while i < n-1 and interval_to_merge[1] >= intervals[i+1][0]:
                # overlap
                interval_to_merge[1] = max(interval_to_merge[1], intervals[i+1][1])
                i += 1

            merged_intervals.append(interval_to_merge)
            i += 1

        return merged_intervals
        '''




        
        
