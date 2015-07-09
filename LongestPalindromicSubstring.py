##class Solution:
##    # @return a string
##    # TLE
##    def longestPalindrome(self, s):
##        l=len(s)
##        if l==0:
##            return None
##        # d[i][j] is whether s[i:j+1] is palindrome
##        d=self.isPalindrome(s)
##        # e[i] is the max length of palindrome of s[i:]
##        e=[1 for i in range(l)]
##        for i in range(l):
##            for j in range(l-1,i,-1):
##                if d[i][j]:
##                    e[i]=j-i+1
##                    break
##        maxS=s[0]
##        maxL=1
##        for i in range(l):
##            if e[i]>maxL:
##                maxL=e[i]
##                maxS=s[i:i+maxL]
##        return maxS
##    def isPalindrome(self,s):
##        l=len(s)
##        d=[[j<=i for j in range(l)] for i in range(l)]
##        for k in range(1,len(s)):
##            for i in range(len(s)-k):
##                if s[i]!=s[i+k]:
##                    d[i][i+k]=False
##                    continue
##                d[i][i+k]=d[i+1][i+k-1]
##        return d

class Solution:
    def longestPalindrome(self, s):
        index=0
        length=0
        for i in range(len(s)):
            if self.isPalindrome(s[i-length:i+1]):
                index=i-length
                length=length+1
            elif i-length-1>=0 and self.isPalindrome(s[i-length-1:i+1]):
                index=i-length-1
                length=length+2
        return s[index:index+length]
    def isPalindrome(self,s):
        return s==s[::-1]
    
s='abac'
print(Solution().longestPalindrome(s))
