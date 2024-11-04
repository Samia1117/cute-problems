class Solution:
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    
        n = len(intervals)
        if not intervals or n == 0:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=False)

        meeting_rooms = [sorted_intervals[0][1]]      # min heap based on end times of meetings
        heapq.heapify(meeting_rooms)

        for i in range(1, n):
            curr_interval = sorted_intervals[i]
            print("Meeting rooms = ", meeting_rooms)
            earliest_availability = meeting_rooms[0]
            print("Earliest_availability: ", [earliest_availability ])
            print("\n")

            # If earliest_availability is after start time of current interval, need a new meeting room
            if earliest_availability > curr_interval[0]:
                heapq.heappush(meeting_rooms, curr_interval[1]) # push the endtime of the current meeting as earliest availability of this new meeting room
            else:
                min_elt = heapq.heappop(meeting_rooms)
                heapq.heappush(meeting_rooms, curr_interval[1])
                # meeting_rooms[0] = curr_interval[1]

        return len(meeting_rooms)





        
