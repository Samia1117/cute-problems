class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # let dp[i][j] = longest palindrome substring starting at char i and ending at char j
        # need longest sequence s[i:j+1]

        n = len(s)
        if (n == 0):
            return ""

        dp = [ [ True if i==j else False for i in range(n)] for j in range(n)]
        maxLen = 1
        result = s[0]
        # Two pointers: left, right.
        for diff in range(1, n):
            # First check all 2 character palindromes, then 3 char, then 4 .. and so on
            for left in range(n-diff):
                # Right pointer is "diff" amount ahead of left
                right = left + diff
                # DP table is built up in a diagonal fashion. This ensures we look at 3 char sequences only once we have values (True/False) values for all possible 2 character sequences
                if (s[left] == s[right] and dp[left + 1 ][right - 1] == True) or (s[left] == s[right] and right - left == 1):
                    dp[left][right] = True

                    # Length of this new palindrome = s[left:right+1]
                    palindrome_len = len(s[left:right+1])
                    if palindrome_len > maxLen:
                        maxLen = palindrome_len
                        result = s[left:right+1]
                        # print("new palindrome: ", result)

        return result

