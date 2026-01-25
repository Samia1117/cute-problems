from collections import defaultdict
from heapq import heapify, heappush, heappop

class Leaderboard:

    def __init__(self):
        self.leaderbaord = defaultdict(list)
        self.top_k_queue = []
        heapify(self.top_k_queue)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderbaord:
            self.leaderbaord[playerId] = 0
        self.leaderbaord[playerId] += score

    def top(self, K: int) -> int:
        # print(f'Finding top k for leaderboard = {self.leaderbaord} with k = {K}')
        # items = sorted(self.leaderbaord.items(), key = lambda x: x[1], reverse=True)[:K]
        # return sum([i[1] for i in items])
        
        k_heap = []
        heapify(k_heap)

        idx = 0
        for k,v in self.leaderbaord.items():
            heappush(k_heap, v)
            if len(k_heap) > K:
                heappop(k_heap)
        res = 0
        while k_heap:
            res += heappop(k_heap)
        return res


    def reset(self, playerId: int) -> None:
        self.leaderbaord[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
