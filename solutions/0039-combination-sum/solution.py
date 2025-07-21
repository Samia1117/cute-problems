class Solution:

    valid_combs = []

    def combSumRec(self, candidates, currTarget, comb):
        if currTarget < 0:
            return
        if sum(comb) > 150:
            return 
        if currTarget == 0:
            # this combination achieves target
            self.valid_combs.append(comb)
            return

        for i in range(len(candidates)):
            candidate = candidates[i]
            new_comb = comb.copy()
            new_comb[i] += 1
            self.combSumRec(candidates, currTarget - candidate, new_comb)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.valid_combs = []
        comb = [0 for i in range(len(candidates))]
        self.combSumRec(candidates, target, comb)

        results = []
        results_set = set([])
        for comb in self.valid_combs:
            res = []
            for elt_indx, elt in enumerate(comb):
                for i in range(elt):
                    res.append(candidates[elt_indx])
            res_str = "-".join([str(a) for a in res])
            if res_str not in results_set:
                results.append(res)
                results_set.add(res_str)
        print(f'results = {results}')
        return results
        # return self.valid_combs
        
