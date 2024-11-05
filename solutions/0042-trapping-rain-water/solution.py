class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        size = len(height)
        # Initialize arrays where 
        # left[i] = max height in height[0:i+1] (including height[i])
        left_maxes = [0 for _ in range(size)]
        # right[i] = max height in height[i:] (including height[i])
        right_maxes = [0 for _ in range(size)]

        # Base cases - max height to the left of first entry is itself and max height to the right of last entry is itself
        left_maxes[0] = height[0]
        right_maxes[size-1] = height[size-1]

        # Fill out the rest of the dp table
        for i in range(1, size):
            left_maxes[i] = max(left_maxes[i-1], height[i])
        
        for i in reversed(range(size-1)):
            right_maxes[i] = max(right_maxes[i+1], height[i])
        
        for i in range(1, size - 1):
            # Find the highest wall to the left of this bar
            left_max = left_maxes[i-1]
            # Find the highest wall to the right of this bar
            right_max = right_maxes[i+1]

            # if we have higher walls on both sides, then for this 'row'(1 unit) the column of water above it is min(left_max, right_max) -  height of this wall 
            if left_max > height[i] and right_max > height[i]:
                ans += min(left_max, right_max) - height[i]
        return ans
        
