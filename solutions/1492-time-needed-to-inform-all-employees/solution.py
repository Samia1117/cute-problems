class Solution:
    
    def maxTime(self, i, informTime, d):
        maxFromThisPoint = 0
        if i not in d:
            return maxFromThisPoint

        for child in d[i]:
            time = self.maxTime(child, informTime, d) + informTime[i]
            maxFromThisPoint = max(time, maxFromThisPoint)

        return maxFromThisPoint
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # start at headID
        # if you try a local minimum, might not be a global minimum
        # try every employee and those they manage
        # for each manager[i], put manager[i]:[i, ..] since manager[i]
        # manages employee i (manager=parent, managed=children)
        
        d = {}  # adjacency dict
        
        for i,man in enumerate(manager):
            if man==-1:
                continue
            if man not in d:
                d[man] = []
            d[man].append(i)
        
        if not d:
            return informTime[headID]
        
        return self.maxTime(headID, informTime, d)
            
        
        
        
        
        
        
        
        
        
