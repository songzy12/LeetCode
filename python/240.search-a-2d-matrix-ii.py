class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        # each column from top to bottom ascending
        if not matrix:
            return False
        m,n = len(matrix), len(matrix[0])
        i,j = 0,n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
        
##    def binarySearchRow(self, left, right, target, matrix):
##        if left == right:
##            return left
##        #middle = (left + right)//2
##        print(left, middle, right)
##        if matrix[middle][0] > target:
##            return self.binarySearchRow(left, middle, target, matrix)
##        if matrix[middle+1][0] <= target:
##            return self.binarySearchRow(middle+1, right, target, matrix)
##        return middle
##    def binarySearchColumn(self, left, right, target, row):
##        if left == right:
##            return True if row[left] == target else False
##        #middle = (left + right)//2
##        print(left, middle, right)
##        if row[middle] == target:
##            return True
##        if row[middle] < target:
##            return self.binarySearchColumn(middle+1, right, target, row)
##        if row[middle] > target:
##            return self.binarySearchColumn(left, middle, target, row)
##        
##    def searchMatrix(self, matrix, target):
##        if not matrix:
##            return False
##        row = self.binarySearchRow(0, len(matrix)-1, target, matrix)
##        for i in range(row+1):
##            if self.binarySearchColumn(0,len(matrix[0])-1,target, matrix[i]):
##                return True
##        return False
            

matrix = [[-5]]
target = -5        
matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
target = 5
target = 20
print(Solution().searchMatrix(matrix, target))
