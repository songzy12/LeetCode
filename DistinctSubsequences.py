class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = len(T)
        n = len(S)
        if m > n:
            return 0
        path = [0 for i in range(m+1)]
        path[0] = 1
        for j in range(1, n+1):
            for i in range(m, 0, -1):
                path[i] = path[i] + (path[i-1] if T[i-1]==S[j-1] else 0)
        return path[m]
        
##        # just use the same idea, but not recursive
##        if len(S)<len(T):
##            return 0
##        # we use m[i][j] to denote numDistinct(S[i:],T[j:])
##        m=[[0 for j in range(len(T))] for i in range(len(S))]
##        # m[i][len(T)-1]=S[i:].count(T[len(T)-1])
##        for i in range(len(S)):
##            m[i][len(T)-1]=S[i:].count(T[len(T)-1])
##        for i in range(len(S)-2,-1,-1):
##            for j in range(len(T)-2,-1,-1):
##                # for when len(S[i:])<len(T[j:]), m[i][j]=0
##                if len(S)-i<len(T)-j:
##                    continue
##                m[i][j]=m[i+1][j]+(m[i+1][j+1] if S[i]==T[j] else 0)
##        return m[0][0]
        
##        if len(S)<len(T) or len(T)==0:
##            return 0
##        if len(T)==1:
##            return S.count(T)
##        i=S.find(T[0])
##        return 0 if i==-1 else\
##               self.numDistinct(S[i+1:],T[1:])+self.numDistinct(S[i+1:],T)
        

S='rabbbit'
T='rabbit'
print(Solution().numDistinct(S,T))
