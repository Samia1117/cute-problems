import math
from collections import deque

class Solution:
    def maximumSwap(self, num: int) -> int:

        # right to left pass
        if not num:
            return num
        numlist = list(str(num))

        n = len(numlist)
        if n <= 1:
            return num
    
        max_right_index = [0 for i in range(n)]
        max_right_index[-1] = n-1 #numlist[-1]

        for i in range(n-2, -1, -1):
            # print(f'numlist[i] = {numlist[i]}, max_to_my_right[i+1] = {max_to_my_right[i+1]}')
            if numlist[i] > numlist[max_right_index[i + 1]]:
                max_right_index[i] = i
            else:
                max_right_index[i] = max_right_index[i+1]

        # print("max_right_index = ", max_right_index)

        max_num = numlist[0]
        for i in range(n):
            curr_num = int(numlist[i])
            max_num_to_my_right = int(numlist[max_right_index[i]])

            if curr_num < max_num_to_my_right:
                ## swap
                numlist[i], numlist[max_right_index[i]] = numlist[max_right_index[i]], numlist[i]
                break
        
        # print("numlist = ", numlist)
        return int(''.join(numlist))
