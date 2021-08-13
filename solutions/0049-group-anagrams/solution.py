class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        worddict = {}
        for word in strs:
            sortedword = "".join(sorted(list(word)))
            if sortedword not in worddict:
                worddict[sortedword] = []
            worddict[sortedword].append(word)
            
        #print(worddict)
        # sorts1 = sorted(worddict.items(), key = lambda x: x[0], reverse=False)
        # new = []
        # for tup in sorts1:
        #     vals = tup[1]
        #     new.append(sorted(vals))
        # print(new)
        # return new
        return worddict.values()
