class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        l = []
        for i in s:
            if len(l) and (l[-1], i) in [('(',')'), ('[',']'), ('{','}')]:
                l.pop()
            elif i in [')', ']', '}']:
                return False
            else:
                l.append(i)
        return len(l) == 0
                
print(Solution().isValid('{[]}'))
