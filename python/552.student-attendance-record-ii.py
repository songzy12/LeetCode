class Solution(object):
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        # dp[i]: the number of all possible attendance (without 'A') records with length i
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result
    
##    def __init__(self):
##        p = int(1e9+7)
##        self.m = [[[0 for a in range(2)] for l in range(3)] for n in range(100000+1)]
##        for n in range(100000+1):
##            for l in range(3):
##                for a in range(2):
##                    if n == 0:
##                        self.m[n][l][a] = 1
##                        continue
##                    self.m[n][l][a] = self.m[n-1][0][a] + \
##                                (self.m[n-1][l+1][a] if l < 2 else 0) + \
##                                (self.m[n-1][0][a+1] if a < 1 else 0)
##                    self.m[n][l][a] %= p
##        
##    def checkRecord(self, n):
##        """
##        :type n: int
##        :rtype: int
##        """
##        return self.m[n][0][0]

if __name__ == '__main__':
    n = 99998
    print Solution().checkRecord(n)

# do not use function call, since it has max depth limit
# still TLE

# O(\log n)
# f[i][0][0]   | 0 0 1 0 0 0 |   f[i-1][0][0]
# f[i][0][1]   | 1 0 1 0 0 0 |   f[i-1][0][1]
# f[i][0][2] = | 0 1 1 0 0 0 | * f[i-1][0][2]
# f[i][1][0]   | 0 0 1 0 0 1 |   f[i-1][1][0]
# f[i][1][1]   | 0 0 1 1 0 1 |   f[i-1][1][1]
# f[i][1][2]   | 0 0 1 0 1 1 |   f[i-1][1][2]
