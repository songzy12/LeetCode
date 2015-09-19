class Solution(object):
    def numSquares(self, n):
        squares = [i*i for i in range(int(n**0.5 + 1))]
        for a in squares:
            for b in squares:
                for c in squares:
                    for d in squares:
                        if a+b+c+d == n:
                            return (a>0) + (b>0) + (c>0) + (d>0)
                        
##    def numSquares(self, n):
##        dp = [-1 for i in range(n+1)]
##        dp[0] = 0
##        for i in range(1, n+1):
##            j, ans = 1, 1<<30
##            while j * j <= i:
##                ans = min(ans, 1 + dp[i-j*j])
##                j += 1
##            dp[i] = ans
##        return dp[n]
##    1089, TLE
    
##    def __init__(self):
##        self.dp = [0]
##    def numSquares(self, n):
##        if len(self.dp) < n+1:
##            self.dp += [-1 for i in range(len(self.dp), n+1)]
##        if self.dp[n] != -1:
##            return self.dp[n]
##        t, ans = 1, 1<<30
##        while t * t <= n:
##            ans = min(ans, 1 + self.numSquares(n-t*t))
##            t += 1
##        self.dp[n] = ans
##        return self.dp[n]
## 9732, RuntimeError: maximum recursion depth exceeded

for i in range(0, 10):
    print i, Solution().numSquares(i)
