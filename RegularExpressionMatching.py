class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [[False for x in range(len(p)+1)] for j in range(len(s)+1)]
        # dp[i][j] = True means s[:i] matches p[:j]
        dp[0][0] = True
        for j in range(len(p)):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]
        # loop each char in s and p
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]!='*':
                    if dp[i][j] and (s[i] == p[j] or p[j] == '.'):
                        dp[i+1][j+1] = True
                else:
                    if dp[i+1][j-1]:
                        # no p[j-1]
                        dp[i+1][j+1] = True
                    if dp[i][j+1] and (p[j-1] == s[i] or p[j-1] == '.'):
                        # one more p[j-1]
                        dp[i+1][j+1] = True
                print(i+1, j+1, dp[i+1][j+1])
        return dp[len(s)][len(p)]
            
##        if not len(p):
##            return not len(s)
##        if len(p) == 1:
##            return (len(s) == 1 and (True if p[0] == '.' else s[0] == p[0]))
##        if p[1] != '*':
##            return ((s[0] == p[0] if p[0]!='.' else True) and
##                    self.isMatch(s[1:], p[1:]))
##        # p[1] == '*'
##        ps = pp = 0
##        
##        if self.isMatch(s, p[2:]):
##            return True
##        i = 0
##        while i < len(s) and (s[i] == p[0] if p[0]!='.' else True):
##            # ab, .*
##            if self.isMatch(s[i+1:], p[2:]):
##                return True
##            i += 1
##        return False


# aaaaaaaaaaaaab a*a*a*a*a*a*a*a*a*a*c
import sys
stdin, stdout = sys.stdin, sys.stdout
fin = open('_in.txt', 'r')
fout = open('_out.txt', 'w')
sys.stdin, sys.stdout = fin, fout
T = int(input())
while T:
    T -= 1
    s, p = input().split()
    print(Solution().isMatch(s, p))
fin.close()
fout.close()
sys.stdin, sys.stdout = stdin, stdout
