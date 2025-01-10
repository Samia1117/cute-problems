class Solution:
    # @cache
    def isPalindrome(self, s, i, j):
        if len(s) <= 1:
            return True
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        i, j = 0, n-1
        while i < j:
            # print(f's = {s}, i={i}, j={j}')
            if s[i] != s[j]:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True
