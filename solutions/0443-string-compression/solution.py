class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count_map = OrderedDict()
        
        n = len(chars)
        if n <= 1:
            return n
        
        idx = 0
        curr_streak = 0
        prev_char = chars[0]

        for i in range(n):
            curr_char = chars[i]
            # print(f'prev_char, curr_char = {prev_char}, {curr_char}')

            if curr_char == prev_char:
                curr_streak += 1
                if i == n-1:
                    chars[idx] = prev_char
                    idx += 1
                    if curr_streak > 1:
                        if curr_streak > 9:
                            curr_streak = str(curr_streak)
                            for digit in curr_streak:
                                chars[idx] = digit
                                idx += 1
                        else:
                            chars[idx] = str(curr_streak)
                            idx += 1
            else:
                print(f' ### breaking streak at {curr_streak}')
                # end of streak - encode until prev char
                chars[idx] = prev_char
                idx += 1
                if curr_streak > 1:
                    if curr_streak > 9:
                        curr_streak = str(curr_streak)
                        for digit in curr_streak:
                            chars[idx] = digit
                            idx += 1
                    else:
                        chars[idx] = str(curr_streak)
                        idx += 1
                    # print(f'chars = {chars}')
                if i == n-1:
                    chars[idx] = curr_char
                    idx += 1



                curr_streak = 1
                prev_char = curr_char

        return idx
        

