class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[-1 for i in range(len(word2)+1)] for i in range(len(word1)+1)]
        def get(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == 0 or j == 0:
                dp[i][j] = 0
                return dp[i][j]
            if word1[i-1] == word2[j-1]:
                dp[i][j] = max(get(i-1,j), get(i,j-1), get(i-1,j-1)+1)
                return dp[i][j]
            dp[i][j] = max(get(i-1,j), get(i,j-1))
            return dp[i][j]
        return len(word1)+len(word2)-2*get(len(word1),len(word2))
            
            
            
