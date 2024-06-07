class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        from string import upper
        S = map(upper, filter(lambda x: x!='-', S))
        return '-'.join(reversed([''.join(S[i-K if (i-K) > 0 else 0:i]) for i in range(len(S), 0, -K)]))

S = "2-4A0r7-4k"
K = 0
print Solution().licenseKeyFormatting(S, K)
