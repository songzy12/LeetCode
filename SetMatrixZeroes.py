class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, column = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    row += i,
                    column += j,
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in column:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        return

matrix = [[1,3,4],
          [2,0,1],
          [3,2,6]]
Solution().setZeroes(matrix)
for r in matrix:
    print r
                
                
