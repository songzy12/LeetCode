class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # since dp[i][j] = max(2+dp[i+1][j-1], dp[i][j-1], dp[i+1][j])
        # so for i in reversed(range(len(s))), for j in range(len(s))
        dp = [[0 for j in range(len(s))] for i in range(2)]        
        for i in reversed(range(len(s))):
            for j in range(i,len(s)):
                if j == i:
                    dp[i%2][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i%2][j] = dp[(i+1)%2][j-1]+2 if i+1<=j-1 else 2
                    # no need to compare with dp[i+1][j] or dp[i][j-1]
                else:
                    dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
        return dp[0][len(s)-1]
    
    #===========================================================================
    # def longestPalindromeSubseq(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     d = {}
    #     def f(s):
    #         if s not in d:
    #             maxL = 0    
    #             for c in set(s):
    #                 i, j = s.find(c), s.rfind(c)
    #                 maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
    #             d[s] = maxL
    #         return d[s]
    #     return f(s)
    #===========================================================================
    
    #===========================================================================
    # def __init__(self):
    #     self.dp = {}
    #     
    # def get_or_set(self, s, i, j):
    #     if (i,j) in self.dp:
    #         return self.dp[(i,j)]
    #     if i > j:
    #         return 0
    #     if i == j:
    #         return 1
    #     if s[i] == s[j]:
    #         self.dp[(i,j)] = max(2 + self.get_or_set(s, i+1, j-1),
    #                              self.get_or_set(s, i, j-1),
    #                              self.get_or_set(s, i+1, j)) 
    #     else:
    #         self.dp[(i,j)] = max(self.get_or_set(s, i, j-1),
    #                              self.get_or_set(s, i+1, j))
    #     return self.dp[(i,j)]
    #     
    # def longestPalindromeSubseq(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     return self.get_or_set(s, 0, len(s)-1)
    #===========================================================================

if __name__ == "__main__":
    s = "bbbab"
    print Solution().longestPalindromeSubseq(s)
    
# dp, O(n^2) time, O(n^2) space

# MLE: change to O(n) Space

# TLE: