class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p:
            return not s
        len_s, len_p = len(s), len(p)
        ptr_s, ptr_p = 0, 0
        tra_s, tra_p = 0, 0
        while ptr_s < len_s:
            # print ptr_s, ptr_p
            if ptr_p < len_p and (p[ptr_p] == '?' or s[ptr_s] == p[ptr_p]):
                ptr_s += 1
                ptr_p += 1
            elif ptr_p < len_p and p[ptr_p] == '*':
            # if elif else
                tra_p = ptr_p + 1 # just the last one
                tra_s = ptr_s + 1
                ptr_p += 1 # ptr_s stays 
            else:
                if tra_p:
                    ptr_p = tra_p
                    ptr_s = tra_s
                    tra_s += 1
                else:
                    return False
        while ptr_p < len_p and p[ptr_p] == '*':
            ptr_p += 1
        return True if ptr_p == len_p else False
        
##        d = [[None for i in range(len(p)+1)] for j in range(len(s)+1)]
##        d[0][0] = True # exam p[0] == '*'
##        if len(p) and p[0] == '*':
##            for k in range(1,len(s)+1):
##                d[k][1] = True 
##        for i in range(1,len(s)+1):
##            d[i][0] = False
##        for j in range(1,len(p)+1):
##            d[0][j] = True if p[:j].count('*') == j else False
##        for i in range(1,len(s)+1):
##            for j in range(1,len(p)+1):
##                #print i,j
##                if d[i][j]!=None:
##                    continue
##                if p[j-1] not in '?*':
##                    d[i][j] = True if p[j-1]==s[i-1] and d[i-1][j-1] else False
##                if p[j-1] == '?':
##                    d[i][j] = True if d[i-1][j-1] else False
##                if d[i][j] and j<len(p) and p[j] == '*':
##                    for k in range(i+1, len(s)+1):
##                        d[k][j+1] = True
##        return d[len(s)][len(p)]

for (s, p) in [('aa','a'), ('aa', 'aa'), ('aaa','aa'),('aa','*'),
               ('aa','a*'), ('ab', '?*'), ('abc','c*a*b*')]:
#s, p = "a", "*?*"
    print(Solution().isMatch(s,p))
