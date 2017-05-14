class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        p = int(1e9+7)
        # do not use the same temp variable as the parameter
        dp = [[[-1 for t0 in range(N+1)] for i0 in range(n)] for j0 in range(m)]
        def get(i0, j0, t0):
            if i0 < 0 or j0 < 0 or i0 >= m or j0 >= n:
                return 0            
            if dp[i0][j0][t0] != -1:
                return dp[i0][j0][t0]
            if t0 <= 0:
                return 0
            if t0 == 1:
                # not only 1 way
                dp[i0][j0][t0] = sum([i0 == 0, j0 == 0, i0 == m-1, j0 == n-1])
                return dp[i0][j0][t0]
            temp = [get(i0-1, j0, t0-1), get(i0+1, j0, t0-1),
                    get(i0, j0-1, t0-1), get(i0, j0+1, t0-1)]
            dp[i0][j0][t0] = sum(temp)
            return dp[i0][j0][t0]
        ans = [get(i, j, t) for t in range(N+1)]
        return sum(ans) % p


m = 2
n = 2
N = 2
i = 0
j = 0

m = 8
n = 50
N = 23
i = 5
j = 26

print Solution().findPaths(m, n, N, i, j)
    
