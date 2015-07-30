class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def dp(self, i, j, k, s1, s2, s3):
        #print(i,j,k)
        if (i,j,k) in self.d:
            return self.d[i,j,k]
        if not i:
            self.d[i,j,k] = s2[:j] == s3[:k]
            return self.d[i,j,k]
        if not j:
            self.d[i,j,k] = s1[:i] == s3[:k]
            return self.d[i,j,k]
        if not k:
            self.d[i,j,k] = False
            return self.d[i,j,k]
        if s1[i-1]!=s3[k-1] and s2[j-1]!=s3[k-1]:
            self.d[i,j,k] = False
            return self.d[i,j,k]
        if s1[i-1]!=s3[k-1]:
            self.d[i,j,k] = self.dp(i,j-1,k-1,s1,s2,s3)
            return self.d[i,j,k]
        if s2[j-1]!=s3[k-1]:
            self.d[i,j,k] = self.dp(i-1,j,k-1,s1,s2,s3)
            return self.d[i,j,k]
        self.d[i,j,k] = self.dp(i-1,j,k-1,s1,s2,s3) or \
                        self.dp(i,j-1,k-1,s1,s2,s3)
        return self.d[i,j,k]
            
    def isInterleave(self, s1, s2, s3):
        self.d = {}
        self.d[0,0,0] = True
        return self.dp(len(s1),len(s2),len(s3),s1,s2,s3)
        
##    def isInterleave(self, s1, s2, s3):
##        if not s1:
##            return s2 == s3
##        if not s2:
##            return s1 == s3
##        if not s3:
##            return not s1 and not s2
##        if s1[0]!=s3[0]:
##            return self.isInterleave(s1, s2[1:], s3[1:])
##        if s2[0]!=s3[0]:
##            return self.isInterleave(s1[1:], s2, s3[1:])
##        return self.isInterleave(s1, s2[1:], s3[1:]) or \
##               self.isInterleave(s1[1:], s2, s3[1:])

##    def isInterleave(self, s1, s2, s3):
##        if len(s1)+len(s2)!=len(s3):
##            return False
##        
##        d = [[[None for i in range(len(s3)+1)]
##              for j in range(len(s2)+1)]
##             for k in range(len(s1)+1)]
##        
##        for k in range(len(s3)+1):
##            for i in range(len(s1)+1):
##                for j in range(len(s2)+1):
##                    if i == j == k == 0:
##                        d[i][j][k] = True
##                        continue
##                    if i and k and d[i-1][j][k-1] and s1[i-1]==s3[k-1] or \
##                       j and k and d[i][j-1][k-1] and s2[j-1]==s3[k-1]:
##                        d[i][j][k] = True
##                    else:
##                        d[i][j][k] = False
##                    #print(i, j, k, d[i][j][k])
##        return d[len(s1)][len(s2)][len(s3)]
        

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s3 = "aadbbbaccc"
s1 = "aabccabc"
s2 = "dbbabc"
s3 = "aabdbbccababcc"
print(Solution().isInterleave(s1,s2,s3))
