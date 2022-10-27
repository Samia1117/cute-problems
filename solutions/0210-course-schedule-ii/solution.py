class Solution:
    
    def __init__(self):
        self.adjDict = {}
        self.recStack = []
        self.visited = set()
        self.postOrder = []
    
    def hasCycle(self, node):
        if node not in self.adjDict:
            self.postOrder.append(node)
            # print("postOrder now: ", self.postOrder)
            return False
        
        self.recStack[node] = True
        for child in self.adjDict[node]:
            if self.recStack[child]==True:
                # print("found child={} in recStack".format(child))
                return True
            if child not in self.visited:
                self.visited.add(child)
                if self.hasCycle(child):
                    # print("found child={} with cycle".format(child))
                    return True
                
        self.recStack[node] = False
        self.postOrder.append(node)
        # print("postOrder now: ", self.postOrder)
        return False
                
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        self.recStack = [False for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        
        for req in prerequisites:
            parent = req[1]
            child = req[0]
            inDegree[child] +=1
            
            if parent not in self.adjDict:
                self.adjDict[parent] = []
            self.adjDict[parent].append(child)
            
            
        # print("adjdict is: ", self.adjDict)
        # print("indegrees are: ", inDegree)
            
        for i in range(numCourses):
            if inDegree[i] == 0:
                self.visited.add(i)
                self.recStack[i] = True
                if self.hasCycle(i):
                    return []
        
        if len(self.postOrder)!=numCourses:
            return []
        # print("post order is: ", self.postOrder)
        return reversed(self.postOrder)
            
            
        
