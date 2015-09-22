class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix) - 1
        while row > 0:
            if matrix[row][0] > target:
                row -= 1
            else:
                break
        for i in matrix[row]:
            if i == target:
                return True
        return False
            
matrix = [[1],[3]]
target = 3
print Solution().searchMatrix(matrix, target)
