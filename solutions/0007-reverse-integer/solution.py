class Solution:
    
    def zero_check(self, new):
        while new[0] == '0':
            if len(new)==1:
                break
            new = new[1:]
        return new
    
    def reverse(self, x: int) -> int:
        strint = str(x)
        new = ""
        if strint[0] == '-':
            new += '-'
            strint = strint[1:]
        l = len(strint)
        for i in range(l):
            new += strint[l-i-1]
            
        # zero check
        if new[0] == '0':
            new = self.zero_check(new)
        elif new[0] == '-' and new[1] == '0':
            new = '-' + self.zero_check(new[1:])

        if int(new) > 2**31 -1 or int(new) <-2**31:
            return 0
        return new
