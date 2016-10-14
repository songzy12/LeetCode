class Solution(object):

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        P = [[False for j in range(len_col)] for i in range(len_row)]
        A = [[False for j in range(len_col)] for i in range(len_row)]

        def bfs(i, j, T):
            T[i][j] = True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= i + x < len_row and 0 <= j + y < len_col and \
                   not T[i+x][j+y] and matrix[i+x][j+y] >= matrix[i][j]:
                    bfs(i + x, j + y, T)
            
        for i in range(len_row):
            bfs(i, 0, P)
        for j in range(len_col):
            bfs(0, j, P)
        
        for i in range(len_row):
            bfs(i, len_col - 1, A)
        for j in range(len_col):
            bfs(len_row - 1, j, A)
        
        ans = []    
        for i in range(len_row):
            for j in range(len_col):
                if A[i][j] and P[i][j]:
                    ans.append([i, j])
        return ans
                
matrix = [[1,2,3],[8,9,4],[7,6,5]]
print Solution().pacificAtlantic(matrix)

# [[1,2,3],[8,9,4],[7,6,5]]
# for P, check from left top will fail
# BFS needed
 
            
