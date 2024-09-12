class Solution:

    def helperIsPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        if s[0] == s[-1]:
            # print(f"New s={s[1:-1]}")
            return self.helperIsPalindrome(s[1:-1])
        else:
            return False
        
    def isPalindrome(self, s: str) -> bool:

        if len(s) <= 1:
            return True

        aset = set('abcdefghijklmnopqrstuvwxyz0123456789')
        cset = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        stripped = ""
        for ch in s:
            if ch in aset:
                stripped += ch
            elif ch in cset:
                stripped += ch.lower()
        

        left, right = 0, len(stripped)
        while right - left >= 2:
            # print(f"New s={stripped[left:right-1]}")
            if stripped[left] == stripped[right-1]:
                left += 1
                right -= 1
            else:
                # print(f"False because s={stripped[left:right-1]}")
                return False
        return True


        # print(f"Stripped = {stripped}")
        # return self.helperIsPalindrome(stripped)
