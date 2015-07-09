class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
##        i = 1
##        n = 0
##        for t in s[::-1]:
##            n = n + (ord(t) - ord('A') + 1) * i
##            i = i * 26
##        return n
        from functools import reduce
        # lambda x, y: 26 * x + y
        return reduce(lambda x, y: 26 * x + y, [ord(c) - 64 for c in list(s)])

print(Solution().titleToNumber('AA'))
            
