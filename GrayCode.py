class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [0] if not n else self.grayCode(n-1)+\
               [(1<<(n-1))+i for i in self.grayCode(n-1)[::-1]]

print Solution().grayCode(2)
        
