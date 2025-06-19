class Solution:
    def canEatAll(self, piles, k: int, h: int) -> int:
        hours_needed = 0
        for pile in piles:
            hours_needed += pile // k if pile % k == 0 else pile // k + 1

        if hours_needed > h:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_k = max(piles)
        
        last_k = max_k
        k = 0

        low, mid, high = 1, (max_k//2), max_k
        while low < high:
            if self.canEatAll(piles, mid, h):
                high = mid
            else:
                low = mid

            mid = (high + low) // 2

            if high - low == 1:
                if self.canEatAll(piles, low, h):
                    return low
                return high

        return low

        
