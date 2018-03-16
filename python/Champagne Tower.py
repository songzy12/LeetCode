# https://leetcode.com/contest/weekly-contest-75/problems/champagne-tower/
class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0 for i in range(101)] for j in range(101)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] <= 1:
                    continue
                else:
                    dp[i+1][j] += (dp[i][j] - 1) / 2 # NOTE: be careful
                    dp[i+1][j+1] += (dp[i][j] - 1) /2
                    dp[i][j] = 1
        return dp[query_row][query_glass]

poured = 4
query_row = 2
query_glass = 1
print(Solution().champagneTower(poured, query_row, query_glass))
