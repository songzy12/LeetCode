class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # use a matrix and DP to find all the palindrome substring.
        # it is more convenient than keep a substring and exam each time
        if len(s)==0:
            return ['']
        isPalindrome=[[False for j in range(len(s))] for i in range(len(s))]
        # if i>=j, then isPalindrome[i][j] is True        
        for j in range(len(s)):
            for i in range(j,len(s)):
                isPalindrome[i][j]=True
        # be careful about the order to initialize!!!
        for k in range(1,len(s)):
            for i in range(len(s)-k):
                j=i+k
                isPalindrome[i][j]=True\
                                    if (s[i]==s[j] and isPalindrome[i+1][j-1])\
                                    else False
        l=[]
        self.auxPartition(s, isPalindrome, [], 0, 1, l)
        return l
    def auxPartition(self, s, isPalindrome, p, i, j, l):
        # p denote the current list
        # i,j denote s[i:j]
        if j==len(s):
            if isPalindrome[i][j-1]:
                p.append(s[i:j])
                l.append(p)
            return
        self.auxPartition(s, isPalindrome, p[:], i, j+1, l)

        if isPalindrome[i][j-1]:
            p.append(s[i:j])
            self.auxPartition(s, isPalindrome, p[:], j, j+1, l)
            return
        

##    # if define a global l, will get OLE in oj
##    # but now, it is TLE
##    def partition(self, s):
##        l=[]
##        self.auxPartition(s, 0, [],'', l)
##        return l
##    def auxPartition(self, s, index, p, t, l):
##        # index denote where we are
##        # s denote the original string
##        # p denote the current list
##        # t denote the current substring
##        
##        # if it is the end of s
##        if index==len(s):
##            if t==''.join(reversed(t)):
##                p.append(t)
##                l.append(p)
##            return
##        # if it is not the end
##        # be careful to use p[:]!!!
##        self.auxPartition(s, index+1, p[:], t+s[index], l)
##        if t!='' and t==''.join(reversed(t)):
##            p.append(t)
##            self.auxPartition(s, index+1, p[:], s[index], l)
##            return

s='abbab'
print(Solution().partition(s))
