# https://leetcode.com/contest/weekly-contest-250/problems/maximum-number-of-points-with-cost/
#
# TLE

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        dp = {}

        def compute(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i == m - 1:
                return points[i][j]

            result = None
            for s in range(n):
                cur_result = points[i][j] + compute(i+1, s) - abs(j - s)
                if not result:
                    result = cur_result
                else:
                    result = max(result, cur_result)
            dp[i, j] = result
            return result
        return max([compute(0, i) for i in range(n)])
