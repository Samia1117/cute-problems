class Solution:
    
    def dfsCycle(self, adjDict, node, visited, recStack):
        
        visited.add(node)
        recStack.add(node)
        
        for neighbor in adjDict[node]:
            if neighbor in recStack:
                return True
            if neighbor not in visited:
                if self.dfsCycle(adjDict, neighbor, visited, recStack):
                    return True
        
        #print("recStack, visited were: ", [recStack, visited])
        # Done with current path from node -> end 
        recStack.remove(node)
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # treat prerequisites[i] as an edge of a graph
        # if graph has cycle, then can not finish
        
        # check for cycle: if node refers to one of its ancestors,
        # then there is a cycle. 
        # Ancestor: in the same path as the current dfs
        
        if prerequisites == []:
            return True
        
        adjDict = {}
        hasPrereq = set()
        
        for p in prerequisites:
            prereq = p[1]
            other = p[0]
            
            if prereq == other: # self-loop
                return False
            
            if prereq not in adjDict:
                adjDict[prereq] = []
            adjDict[prereq].append(other)
            
            if other not in adjDict:
                adjDict[other] = []
                
            hasPrereq.add(other)
            
        allNodes = adjDict.keys()
        
        roots = list(set(allNodes) - hasPrereq)
        if len(roots) == 0:
            return False
        
        megaVisited = set()
        # Now find a root/vertex with in-degree = 0
        for root in roots:
            recStack = set([root])
            visited = set([root])
            
            # Now dfs
            for neighbor in adjDict[root]:
                # visited = set([root])
                if self.dfsCycle(adjDict, neighbor, visited, recStack):
                    return False
                else:
                    print("visited is: ", visited)
            megaVisited.update(visited)
        
        if len(megaVisited) != len(allNodes):
            return False
        return True
        
