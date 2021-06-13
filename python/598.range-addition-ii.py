class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops: # boarder condition
            return m * n 
        return min([x[0] for x in ops]) * min([x[1] for x in ops])

    
