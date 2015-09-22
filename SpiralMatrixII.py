class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for j in range(n)] for i in range(n)]
        cur, i, j = 1, 0, 0
        while cur < n*n:
            t = i
            while j < n-t-1:
                matrix[i][j] = cur
                cur += 1
                j += 1
            while i < n-t-1:
                matrix[i][j] = cur
                cur += 1
                i += 1
            while j > t:
                matrix[i][j] = cur
                cur += 1
                j -= 1
            while i > t:
                matrix[i][j] = cur
                cur += 1
                i -= 1
            i += 1
            j += 1
        if n % 2:
            matrix[n//2][n//2] = n*n
        return matrix

m = Solution().generateMatrix(6)
for row in m:
    print row
        
