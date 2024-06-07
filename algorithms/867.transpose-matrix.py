class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)

A = [[1,2,3],[4,5,6],[7,8,9]]
print Solution().transpose(A)
        
