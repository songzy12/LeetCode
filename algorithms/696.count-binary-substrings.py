class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def compute(i):
            res = 0
            while i - res >= 0 and i + 1 + res < len(s):
                if res == 0:
                    if s[i - res] == s[i + 1 + res]:
                        break
                else:
                    if s[i - res] != s[i - res + 1] or \
                       s[i + 1 + res] != s[i + res]:
                        break
                res += 1
            return res
            
        
        ans = 0
        for i in range(len(s)):
            ans += compute(i)
        return ans

s = "10101"
print Solution().countBinarySubstrings(s)
