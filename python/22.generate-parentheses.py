class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        l=[]
        nleft=0
        nright=0
        self.auxGenerateParenthesis(l, nleft, nright, n, '')
        return l
    def auxGenerateParenthesis(self, l, nleft, nright, n, s):
        if nleft==n:
            while nright<n:
                s+=')'
                nright+=1
            l.append(s)
        # nleft < n and nleft == nright:
        else:
            if nleft == nright:
                self.auxGenerateParenthesis(l, nleft+1, nright, n, s+'(')
        # nleft < n and nleft > nright:
            else:
                self.auxGenerateParenthesis(l, nleft+1, nright, n, s+'(')
                self.auxGenerateParenthesis(l, nleft, nright+1, n, s+')')
            
print(Solution().generateParenthesis(3))
