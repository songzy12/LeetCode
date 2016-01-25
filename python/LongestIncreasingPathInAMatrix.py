class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memo = {}
        matrix = {i+j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        def length(z):
            if z not in memo:
                memo[z] = 1 + max([length(Z)
                                   for Z in z+1, z-1, z+1j, z-1j
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0]) 
            return memo[z]
        return max(map(length, matrix) or [0])

matrix = [[3,4,5],
          [3,2,6],
          [2,2,1]]
print Solution().longestIncreasingPath(matrix)
