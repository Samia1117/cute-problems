import random
class Solution:

    def binary_search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # print(f"low, high, mid = {low}, {high}, {mid}")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                if low == mid:
                    low = mid + 1
                else:
                    low = mid

        return low

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        curr_sum = 0
        for num in w:
            curr_sum += num
            self.prefix_sums.append(curr_sum)
        self.total_sum = curr_sum

    def pickIndex(self) -> int:
        random_sum = random.random() * self.total_sum
        # print(f'random_sum={random_sum}')
        # print(f'self.prefix_sums. ={self.prefix_sums}')

        index = self.binary_search(self.prefix_sums, random_sum)
        # print(f"Obtained index = {index}")
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
