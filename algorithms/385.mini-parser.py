# Given a nested list of integers represented as a string,
# implement a parser to deserialize it.
# Each element is either an integer, or a list --
# whose elements may also be integers or other lists.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
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

class Solution(object):
    def deserialize_core(self, data_list):
        if isinstance(data_list, list):
            nested_integer = NestedInteger()
            for n in data_list:
                nested_integer.add(self.deserialize_core(n))
            return nested_integer
        else:
            return NestedInteger(data_list)

    def deserialize(self, s):
        data = eval(s)
        return self.deserialize_core(data)

# first thought: use split ','
# second thought: use a stack
# use eval, no need for stack and split
