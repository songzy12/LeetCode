class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {} # no need to use lists

        def get_dp(i, j): # use as less state as possible
            if i > j:
                return 0
            if (i, j) in dp:
                return dp[i, j]
            ans = get_dp(i, j-1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    ans = min(ans, get_dp(i, k-1) + get_dp(k+1, j))
            dp[i, j] = ans
            return ans
        
##        def get_dp(i, j, k):
##            # index from i to j, with k same color with s[j] to the right
##            if i > j:
##                return 0
##            if (i, j, k) in dp:
##                return dp[i, j, k]
##            while j > 0 and s[j-1] == s[j]:
##                j -= 1
##                k += 1
##            #print i, j, k
##            ans = get_dp(i, j-1, 0) + 1 # the first brush is from j to j
##            for t in range(i, j):
##                if s[t] == s[j]: # the fitst brush is from j to t
##                    ans = min(ans, get_dp(i, t, k+1) + get_dp(t+1, j-1, 0))
##            dp[i, j, k] = ans
##            return ans
        return get_dp(0, len(s)-1)

s = "ydfatmztyqgmuxjedlxcaftgflhuqldooiqjxqfvinjcksgqeguglnosavorgrhxcaizsnwabfcnalfgrzmepaypxniegsdisljk"
s = "cbcbddaccadbdcccaddcccccacdcabddaabacccbdaabcb"
print Solution().strangePrinter(s)
