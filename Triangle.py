class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]
        for i in range(len(dp)-2, -1, -1):
            # print dp
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print Solution().minimumTotal(triangle)
