class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        d = collections.Counter(s)
        res = []
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():
            res.append(x[0] * d[x[-1]])
            for c in x:
                d[c] -= d[x[-1]]
        return ''.join(sorted(res))

s = ''
print Solution().originalDigits(s)

# for zero, it's the only word has letter 'z',
# for two, it's the only word has letter 'w',
