class Solution:
    def fib(self, n: int) -> int:

        if n == 0 or n == 1:
            return n
        
        f = [0 for i in range(n+1)]
        f[1] = 1

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

        # return self.fib(n-1) + self.fib(n-2)
        
