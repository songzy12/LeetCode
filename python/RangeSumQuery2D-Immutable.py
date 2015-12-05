class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.m = []
            return
        self.m = [[0 for i in range(len(matrix[0])+1)]
                  for j in range(len(matrix)+1)]
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                self.m[i][j] = matrix[i][j] + self.m[i+1][j] + \
                               self.m[i][j+1] - self.m[i+1][j+1]
        # for row in self.m:
        #     print row

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.m:
            return 0
        return self.m[row1][col1] - self.m[row1][col2+1] - \
               self.m[row2+1][col1] + self.m[row2+1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
matrix = []
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3) # == 8
print numMatrix.sumRegion(1, 1, 2, 2) # == 11
print numMatrix.sumRegion(1, 2, 2, 4) # == 12
