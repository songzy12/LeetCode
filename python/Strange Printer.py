class Solution(object):
    def __init__(self):
        length = 105
        self.dp = [[[-1 for i in range(length)] for j in range(length)] for k in range(length)]
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = self.dp
        def get_dp(i, j, k):
            # index from i to j, with k same color with s[j] to the right
            if i > j:
                return 0
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            while j > 0 and s[j-1] == s[j]:
                j -= 1
                k += 1
            #print i, j, k
            ans = get_dp(i, j-1, 0) + 1 # the first brush is from j to j
            for t in range(i, j):
                if s[t] == s[j]: # the fitst brush is from j to t
                    ans = min(ans, get_dp(i, t, k+1) + get_dp(t+1, j-1, 0))
            dp[i][j][k] = ans
            return ans
        return get_dp(0, len(s)-1, 0)

s = "ydfatmztyqgmuxjedlxcaftgflhuqldooiqjxqfvinjcksgqeguglnosavorgrhxcaizsnwabfcnalfgrzmepaypxniegsdisljk"
print Solution().strangePrinter(s)
