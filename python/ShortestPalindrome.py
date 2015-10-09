class Solution:
##    # Rabin-Karp algorithm: hash function
##    # KMP algorithm
##    def shortestPalindrome(self, s):
##        l = s + '#' + s[::-1]
##        p = [0 for i in range(len(l))]
##        # p[q]: length of longest prefix && suffix of l[0...q]
##        # l[0:p[q]] == l[q-p[q]+1:q+1]
##        k = 0
##        for q in range(1, len(l)):
##            while k > 0 and l[q] != l[k]:
##            # keep shifting to longest suffix until matching
##                k = p[k-1] 
##            if l[q] == l[k]:
##                k += 1
##            p[q] = k
##        #print(l)
##        #print(p)
##        return s[::-1][:len(s)-p[len(l)-1]] + s

    # Manacher's algorithm
    def shortestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        t = ['#' for i in range(2*n+3)]
        t[0] = '^' # avoid bound check
        t[-1] = '$'
        for i in range(1, n+1):
            t[2*i] = s[i-1]
        # print(t)
        n = 2*n+3
        P = list(range(n))
        C = R = 0
        for i in range(1, n):
            i_mirror = 2*C - i
            P[i] = min(R-i, P[i_mirror]) if R > i else 0
            while i+1+P[i] < n and t[i+1+P[i]] == t[i-1-P[i]]: # compare char beyond R
                P[i] += 1;
            if i + P[i] > R:
                C = i
                R = i + P[i]
        maxLen = centerIndex = 0
        for i in range(n-1, -1, -1):
            if 1 == i - P[i]: # start from ^
                maxLen = P[i]
                break
        return s[maxLen:][::-1] + s
        
        
s = "abc"
print(Solution().shortestPalindrome(s))
