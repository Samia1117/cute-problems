class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        curr_streak = set([])
        max_seq = 0
        # left, right = 0, 0
        left = 0
# 

        for right in range(n):
            while s[right] in curr_streak:
                curr_streak.remove(s[left])
                left += 1
            curr_streak.add(s[right])
            max_seq = max(max_seq, (right - left + 1))
        return max_seq
        '''
        while right < n:
            # max_seq = max(max_seq, len(curr_streak))
            # print(f'curr_streak = {curr_streak}')
            # print(f'curr_seq = {s[left:right+1]}')
            # print(f'max_seq = {max_seq}')
            max_seq = max((right - left + 1), max_seq)

            if s[right] in curr_streak:
                while s[left] != s[right]:
                    curr_streak.remove(s[left])
                    left += 1
                # now s[left] == s[right] e.g. a*bca*
                if left < n:
                    # remove the duplicate char
                    curr_streak.remove(s[left])
                    # shrink the window
                    left += 1
            else:
                # expand the window
                curr_streak.add(s[right])
                right += 1

        # max_seq = max(max_seq, len(curr_streak))
        return max_seq
        '''
