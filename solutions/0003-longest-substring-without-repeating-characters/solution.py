class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == None:
            return 0

        n = len(s)
        if n == 0:
            return 0

        hmap = {}
        max_length = 0
        current_length = 0

        index = 0

        while index < n:
            ch = s[index]
            # if haven't seen this character in current substring iteration
            if ch not in hmap:
                hmap[ch] = index
                current_length += 1
            # have seen this character before in current substring iteration
            else:
                max_length = max(max_length, current_length)

                # start new substring from where this character was last seen + 1
                index = hmap[ch] + 1
                if index == n:
                    break
                # reset current substring length and hashmap
                current_length = 0
                hmap = {}

                # don't increment index below
                continue

            index += 1

        max_length = max(max_length, current_length)
        # print("hmap: ", hmap)

        return max_length
