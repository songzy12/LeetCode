class Solution(object):
    def __init__(self):
        self.preorder = []
        
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        self.preorder = preorder.split(",")
        # print self.preorder
        res = self.isValidSerializationHelper(0)
        return res == len(self.preorder)
        
    def isValidSerializationHelper(self, index):
        if index >= len(self.preorder) or index < 0:
            return -1
        if self.preorder[index] == '#':
            return index + 1
        index_ = self.isValidSerializationHelper(index + 1)
        return self.isValidSerializationHelper(index_)

preorder = "9,#,#,1"
print Solution().isValidSerialization(preorder)
        
