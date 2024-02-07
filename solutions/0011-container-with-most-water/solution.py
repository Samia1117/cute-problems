class Solution:
    def maxArea(self, height: List[int]) -> int:

        if height == None or height == []:
            return 0
        
        n = len(height)
        left, right = 0, n - 1

        maxArea = 0
        while (right != left):
            w = right - left
            newMaxArea = w * min(height[left], height[right])
            maxArea = max(maxArea, newMaxArea)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
        
