class Solution:

    @cache
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x, -n)
            
        else:
            if n%2 == 0:
                return self.myPow(x, n/2) * self.myPow(x, n/2)
            else:
                n_half_floor = n//2
                n_half_ceil = n_half_floor + 1

                return self.myPow(x, n_half_floor) * self.myPow(x, n_half_ceil)

        
