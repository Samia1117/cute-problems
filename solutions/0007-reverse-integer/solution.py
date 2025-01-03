class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if abs(x) != x:
            x = abs(x)
            negative = True

        rev = 0
        while x:
            x, rem = divmod(x, 10)
            rev = rev * 10 + rem
            if rev > 2**31 - 1:
                return 0

        if negative:
            rev = -1 * rev
        print("rev = ", rev)
        return rev
        
