class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        if not heights:
            return []
        
        n = len(heights)
        max_to_my_right = [0] * n
        # max_to_my_right[-1] = heights[-1]

        for i in range(n-2, -1, -1):
            max_to_my_right[i] = max(max_to_my_right[i+1], heights[i+1])
        # print(f"heights = {heights}")
        # print(f'max_to_my_right = {max_to_my_right}')
        
        ans = []
        for i in range(n):
            my_height = heights[i]
            max_height_to_right = max_to_my_right[i]
            if my_height > max_height_to_right:
                ans.append(i)
        return ans


        
