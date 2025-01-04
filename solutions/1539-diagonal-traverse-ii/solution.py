class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        # groups = defaultdict(list)
        # for row in range(len(nums) - 1, -1, -1):
        #     for col in range(len(nums[row])):
        #         diagonal = row + col
        #         groups[diagonal].append(nums[row][col])
                
        # ans = []
        # curr = 0
        
        # while curr in groups:
        #     ans.extend(groups[curr])
        #     curr += 1

        # return ans
        diagsum_map = {}
        n = len(nums)

        for i in range(n-1, -1, -1):
            curr_row = nums[i]
            m = len(curr_row)
            for j in range(m):
                idx_sum = i + j
                if idx_sum not in diagsum_map:
                    diagsum_map[idx_sum] = []
                diagsum_map[idx_sum].append(curr_row[j])
            
        # print("diagsum_map = ", diagsum_map)
        
        ret = []
        currSum = 0

        while currSum in diagsum_map:
            ret.extend(diagsum_map[currSum])
            currSum += 1
        return ret
