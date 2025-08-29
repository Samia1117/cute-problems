class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        rooms_visited = set()

        remaining = set([0])
        seen = set([0])
        i = 0
        while remaining:
            next_idx = remaining.pop()
            for item in rooms[next_idx]:
                if item not in seen:
                    remaining.add(item)
                    seen.add(item)
            if len(seen) == n:
                return True
        return False
        
