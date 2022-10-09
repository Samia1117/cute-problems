class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        # print("target is: ", target)
        # print("candidates are: ", candidates)
        
        dp = [0 for i in range(target+1)] # dp[i] = number of ways to make the sum i: if i=6, dp[i] might be 3 -> "seen"(dict below) will keep track of the actual 3 ways: [2, 2, 2], [3, 3], [6];                      i.e. seen[6] = [[2, 2, 2], [3, 3], [6]], dp[6] = 3

        seen = {}   # dict which maps sum (e.g. 7) to all possible ways to make 7 (using lowest units available): e.g [7], [2, 2, 3]
        for c in candidates:
            if c>target:
                continue
            dp[c] = 1
            seen[c] = []
            seen[c].append([c])
        seen[0] = [[0]]
        if target not in seen:  # corner case
            seen[target] = []
        
        # print("dp:  ", dp)    # check 
        seenlist = []
        minelt = min(candidates)
        for i in range(1, target+1):
            if i<= minelt:
                continue
            for j in range(1, i):
                res = dp[i-j]*dp[j]
                if res!=0:
                    # print("looking at elt = i = ", i)
                    # print("looking at its ancestors: ", [i-j, j])

                    if j in seen and i-j in seen:
                        # print("components it's made up of exists")
                        new_comb =[]
                        for sj in seen[j]:
                            for sij in seen[i-j]:
                                comb = sorted(sj + sij)
                                if comb not in seenlist:
                                        if i not in seen:
                                            seen[i] = [comb]
                                        else:
                                            seen[i].append(comb)
                                        dp[i] +=1
                                        seenlist.append(comb)
                                        # print("found new comb for i,comb = ", [i, comb])
                                else:
                                    pass
                                    # print("this comb = already exists: ", comb)
                    # print("dp now: ", dp)
                    # print("seen now: ", seen)

        
        # print("dp final: ", dp)
        # print("seen final: ", seen)
        
        return seen[target]

        
