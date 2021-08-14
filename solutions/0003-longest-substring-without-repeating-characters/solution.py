class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        runningMax = 0
        seendict = {}
        seen = []
        sequenceStarted = 0
        for i in range(len(s)):
            letter = s[i]
            if letter not in seendict:
                seendict[letter] = i   # where this letter is
                seen.append(letter)
            else:   # found a repeat
                #print("found repeat letter: ",letter, "dict: ", seendict)
                maxForThisSequence = i - sequenceStarted
                if maxForThisSequence >runningMax:
                    runningMax = maxForThisSequence
                #runningMaxes.append(i - sequenceStarted)
                #print("sequence start, end: ", sequenceStarted, i)
                #repeatIndex = seendict[letter]
                sequenceStarted = seendict[letter]+1
                
                #print("reapeat index: ", repeatIndex)
                #print("seen: ", seen)
                
                cutUntil = seen.index(letter)
                #print("cutting until: ", cutUntil)
                toRemove = seen[0:cutUntil+1]
                #print("to remove is: ", toRemove)
                seen = seen[cutUntil+1:]
                #print("new seen is: ", seen)
                while toRemove:
                    del seendict[toRemove.pop()]
                    
                seendict[letter] = i
                seen.append(letter)
                #print("dictionary after change: ", seendict) 
                
        #print("last sequence started:", sequenceStarted)
        #print("final dictionary ", seendict) 
        #runningMaxes.append(len(seendict))
        #print(runningMaxes)
        runningMax = max(len(seendict), runningMax)
        return runningMax
                
