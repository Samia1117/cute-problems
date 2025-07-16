class Solution:
    def getSum(self, a: int, b: int) -> int:

        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            carry = (x & y) << 1
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry
        else:
            while y:
                ans = x ^ y
                borrow = ((~x) & y) << 1
                x, y = ans, borrow

        return x * sign

        
