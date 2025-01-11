class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        n = len(word)
        m = len(abbr)
        if n == 0:
            return False

        while i < n and j < m:
            # print(f'i, j = {i, j}; word[i], abbr[j] = {word[i], abbr[j]}')
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < m and abbr[k].isnumeric():
                    k += 1
                # print(f'abbr[j:k] = {abbr[j:k]}')
                i += int(abbr[j:k])
                j = k
            else:
                return False
        
        return i == n and j == m
            


        
