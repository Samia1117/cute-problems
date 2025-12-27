# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:

    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def depthSumRec(nestedList: List[NestedInteger], depth: int, result: list[int]) -> None:
            if not nestedList:
                return
            for item in nestedList:
                if item.isInteger():
                    result[0] += depth * item.getInteger()
                else:
                    depthSumRec(item.getList(), depth+1, result)
            return 
        
        result = [0]
        depthSumRec(nestedList=nestedList, depth=1, result=result)
        # print(f'Final sum = {result}')
        return result[0]
