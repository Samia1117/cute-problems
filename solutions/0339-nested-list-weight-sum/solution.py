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
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        if len(nestedList) == 0:
            return 0

        ret = 0
        depth = 1
        prevList = nestedList

        while True:
            # isolate the elements at depth i
            elems = [x for x in prevList if x.isInteger()]
            # isolate the lists at depth i - will be used at depth i+1
            lsts = [x for x in prevList if x.getList() != None]

            if len(elems) != 0:
                # sum elems weighted by depth
                ret += sum([x.getInteger() * depth for x in elems])
            if len(lsts) == 0:
                # no more lists, only elems
                break
            else:
                prevList = []
                for lst in lsts:
                    prevList += lst.getList()
            
            # increment depth as we look at next level of lists
            depth += 1
        
        return ret
        
