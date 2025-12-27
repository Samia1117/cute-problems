# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    def flatten(self,  nestedList: list[NestedInteger], result: list[int]) -> None:
        if not nestedList:
            return
        for item in nestedList:
            if item.isInteger():
                result.append(item.getInteger())
            else:
                self.flatten(item.getList(), result)

    def __init__(self, nestedList: list[NestedInteger]):
        self.result = []
        self.flatten(nestedList, self.result)

        self.index = 0
        self.n = len(self.result)

        # print(f'flattened list = {self.result}')
    
    def next(self) -> int:
        if self.index >= self.n:
            raise IndexError('next called but index already reached end of list')
        
        ret = self.result[self.index]
        self.index += 1
        return ret
    
    def hasNext(self) -> bool:
        if self.result and self.index <= self.n-1:
            return True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
