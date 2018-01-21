class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True

        len_row = len(matrix)
        len_col = len(matrix[0])
        def check(i, j):
            head = matrix[i][j]
            x = i
            y = j
            while x < len_row and y < len_col:
                if matrix[x][y] != head:
                    return False
                x += 1
                y += 1
            return True
            
                
        
        for j in range(len(matrix[0])):
            if not check(0, j):
                return False
        for i in range(len(matrix)):
            if not check(i, 0):
                return False
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(Solution().isToeplitzMatrix(matrix))
