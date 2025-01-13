class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        hmap = {}
        i = 0
        for ch in order:
            if ch not in hmap:
                hmap[ch] = i
                i += 1
        
        # existing_keys = set(list(order))
        # all_keys = set(list(s))
        common_keys = [] # existing_keys.intersection(all_keys)

        for item in s:
            if item in hmap:
                common_keys.append(item)
        
        sorted_common_keys = sorted(common_keys, key=lambda ch: hmap[ch])
        # print(f'Sorted s = {sorted_common_keys}')
        
        ans = ''.join(sorted_common_keys)
        for ch in s:
            if ch not in hmap:
                ans += ch
        return ans
