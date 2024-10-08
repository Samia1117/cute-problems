class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # detect if there is overlap between any two intervals in 'intervals'

        # def 'overlap' = interval[i][1] > interval[i+1][0], where i<n-1

        n = len(intervals)
        if n == 0 or n == 1:
            return True

        # sort intervals based on startTime
        intervals = sorted(intervals, key=lambda x:x[0])
        for i in range(n-1):
            # if startTime of next meeting is before the endTime of current meeting, then cannot attend both meetings
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
        
