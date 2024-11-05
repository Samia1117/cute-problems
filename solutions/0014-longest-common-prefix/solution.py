class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        if n == 0:
            return ""
        
        current_index = 0
        m = min([len(strs[i]) for i in range(n)])
        prefix = ""
        
        while True and current_index < m:
            prefixes = [strs[i][current_index] for i in range(n)]
            if len(set(prefixes)) != 1:
                break
            prefix += strs[0][current_index]

            current_index += 1

        return prefix
        
        
