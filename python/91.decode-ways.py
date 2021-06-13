class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1 if s!='0' else 0
        dp = [0 for i in range(len(s)+1)]
        dp[-1] = 1
        dp[-2] = 0 if s[-1]=='0' else 1
        for i in range(len(s)-2, -1, -1):
            dp[i] = (dp[i+1] if s[i]!='0' else 0)+ \
                    (dp[i+2] if (s[i]!='0' and 1<=int(s[i:i+2])<=26) else 0)
        return dp[0]
print Solution().numDecodings('01')
