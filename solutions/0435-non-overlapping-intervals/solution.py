class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        min_delete_needed = 0
        intervals = sorted(intervals, key=lambda x:x[1])

        '''
        prev_interval = intervals[0]
        i = 0
        n = len(intervals)

        while i < n:
            curr_interval = intervals[i]
            if prev_interval[1] > curr_interval[0]: # prev interval ends after curr one begins
                # overlap
                min_delete_needed += 1
                if prev_interval[1] > curr_interval[1]:
                    # delete prev_interval, which ends later
                    prev_interval = curr_interval
                # else:
                #     # delete curr_interval, which ends earlier
                #     continue
            i += 1               
        '''

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] < prev_end:
                # overlap - current starts before previous ends
                min_delete_needed += 1
            else:
                prev_end = curr[1]
        return min_delete_needed 



        
