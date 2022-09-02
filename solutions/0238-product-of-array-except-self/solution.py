class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1.O(N) 2. Without using the '/' operation
        
        # Return: answer[i] = skip nums[i] but product of everything else
        if nums == [] or len(nums)==0:
            return []
        
#         n = len(nums)
#         new_array = [1 for i in range(n)]
        
#         leftMap = {-1:1}
#         rightMap = {n:1}
        
#         for i in range(n):
#             leftMap[i] = leftMap[i-1] * nums[i]
            
#         for i in reversed(range(n)):
#             rightMap[i] = rightMap[i+1] * nums[i]
        
#         for i in range(n):
#             new_array[i] = leftMap[i-1] * rightMap[i+1]
        
#         return new_array
            
    
        n = len(nums)
        arr = [1 for _ in range(n)]

        for i in range(1, n):
            arr[i] = arr[i-1] * nums[i-1]
        
        right = 1
        
        for i in reversed(range(n)):
            arr[i] *=right
            right *=nums[i]
            
        return arr
            








