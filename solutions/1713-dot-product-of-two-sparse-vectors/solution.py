import numpy as np
class SparseVector:

    def __init__(self, nums: List[int]):
        self.encoding_dict = {}

        idx = 0
        n = len(nums)
        while idx < n:
            num = nums[idx]
            if num != 0:
                self.encoding_dict[idx] = num
            idx += 1
        
        print(f"Encoding dict: {self.encoding_dict}")

            
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        common_keys = set(self.encoding_dict.keys()).intersection(
            set(vec.encoding_dict.keys())
            )
        list1 = list(map(self.encoding_dict.get, common_keys))
        list2 = list(map(vec.encoding_dict.get, common_keys))
        return sum([x * y for x,y in zip(list1, list2)])
        # return int(np.dot(list1, list2))
        print(f"common keys = {common_keys}")
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
