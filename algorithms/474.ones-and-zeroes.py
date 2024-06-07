class Solution(object):

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)] # dp[i][j] '0'*i + '1'*j
        for x in strs:
            num0, num1 = x.count('0'), x.count('1')
            for i in range(n - 1, num0, -1):
                for j in range(m - 1, num1, -1):
                    dp[i][j] = max(dp[i - num0][j - num1] + 1, dp[i][j])
        return dp[-1][-1]
            
        
        
