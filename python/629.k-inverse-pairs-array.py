class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        p = 10**9+7
        
        # dp(i, k): n nums left, k inversion
        # dp(i, k) = dp(i-1, k) + ... + dp(i-1, k-(n-i) or 0)

        # if k = 0, return 1
        # if i = 1, return 1 if k < n else 0

        dp = [[0 for i in range(k+1)] for j in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        for j in range(k+1):
            dp[1][j] = 1 if j < n else 0

        for i in range(2, n+1):
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] - (dp[i-1][j-1-(n-i)] if j-1-(n-i) >= 0 else 0)) % p

                # for t in range(j, max(-1, j-(n-i)-1), -1):
                #     dp[i][j] += dp[i-1][t]

        return dp[n][k]

# TLE        

        
n = 123
k = 134

print Solution().kInversePairs(n, k)
