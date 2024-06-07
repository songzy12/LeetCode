class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxsize = 0
        size = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            size[0][j] = 0 if matrix[0][j]=='0' else 1
            maxsize = max(maxsize, size[0][j])
        for i in range(1, m):
            size[i][0] = 0 if matrix[i][0]=='0' else 1
            maxsize = max(maxsize, size[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    # size[i][j]: maximum size of square with right bottom [i][j]
                    size[i][j] = min(size[i-1][j-1], size[i][j-1], size[i-1][j])+1
                    maxsize = max(maxsize, size[i][j])
        for i in size:
            print i
        return maxsize*maxsize
        
matrix = ["11111111",
          "11111110",
          "11111110",
          "11111000",
          "01111000"]
matrix = [list(i) for i in matrix]
print Solution().maximalSquare(matrix)
