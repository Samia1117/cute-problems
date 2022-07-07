class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphset = set("abcdefghijklmnopqrstuvwxyz")
        alphset2 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        digset = set("0123456789")
        # print(alphset)
        # print(digset)
        
        s2 = ""
        for ch in s:
            if ch in digset or ch in alphset:
                s2 += ch
            elif ch in alphset2:
                s2 += ch.lower()
        # print(s2)
        
        while s2:
            if len(s2) >= 2:
                if s2[0] == s2[-1]:
                    s2 = s2[1:-1]
                else:
                    return False
            else:
                break

        return True

