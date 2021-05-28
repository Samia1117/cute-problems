class Solution(object):
    def get_median(self, array):
        size = int(len(array))
        if size == 0:
            return 0
        if size%2 ==0:
            a1 = array[int(size/2)]
            a2 = array[int(size/2) -1]
            median = (a1+a2)/2.0
            return median
        else:
            median = array[int(size//2)]
            return median
        
    def add_max_elts(self, smaller, bigger, combined):
        if len(smaller)==0:
            return combined+bigger
        for i in range(len(smaller)):
            if smaller[0]>bigger[0]:
                return self.add_max_elts(bigger, smaller, combined)
            else:
                to_add = smaller.pop(0)
                combined.append(to_add)
        return combined+bigger

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = []
        median = 0
        if len(nums1) == 0:
            return self.get_median(nums2)
        if len(nums2) == 0:
            return self.get_median(nums1)
        
        if nums1[0]<=nums2[0]:
            combined = self.add_max_elts(nums1, nums2, combined)
        else:
            combined = self.add_max_elts(nums2, nums1, combined)

        result = self.get_median(combined)
        return result
