class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hmap = {}
        max_len = 0

        l, r = 0, 0
        n = len(s)

        while r < n:
            # print("hmap: ", hmap)
            ch = s[r]
            if ch not in hmap:
                hmap[ch] = r
            else:
                max_len = max(r-l + 1, max_len)

                # shrink the window (l, r)
                char_at = hmap[ch]
                while l <= char_at:
                    l += 1
            max_len = max(r - l + 1, max_len)
            hmap[ch] = r
            r += 1

        max_len = max(r - l + 1, max_len)
        return max_len - 1

        
