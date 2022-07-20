# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return n

        mid = n//2
        low = 0
        high = n
        
        while True:
            if (high==mid):
                if isBadVersion(low):
                    return low
                return high
            
            elif (low==mid):
                if isBadVersion(low):
                    return low
                return high
            
            elif (high == mid + 1):
                if isBadVersion(mid):
                    return mid
                return high
            elif (low == mid +1):
                if isBadVersion(low):
                    return low
                return mid
                    
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
            
            mid = (high+low)//2

                
        
