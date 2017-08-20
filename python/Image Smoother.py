class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        if not n:
            return []
        m = len(M[0])
        Q = [[0 for i in range(m)] for j in range(n)]

        def valid(i, j):
            return 0 <= i < n and 0 <= j < m
        
        def average(i, j):
            dir = [[-1, -1], [-1, 0], [-1, 1], [1, 0], [1, -1], [1, 1], [0, -1], [0, 1], [0, 0]]
            cnt = 0
            tot = 0
            for dx, dy in dir:
                if valid(i + dx, j + dy):
                    cnt += 1
                    tot += M[i+dx][j+dy]
            return tot / cnt
            
        for i in range(n):
            for j in range(m):
                Q[i][j] = average(i, j)
        return Q

M = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print Solution().imageSmoother(M)
