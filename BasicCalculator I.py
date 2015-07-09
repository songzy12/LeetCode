class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        num, i = self.getNum(s, 0)
        res = 0
        sigh = 1
        if s[0] == '-':
            i += 1
            sigh = -1
        while i <= len(s):
            if i == len(s):
                res += num * sigh
                break
            op = s[i]
            i += 1
            if op == '+':
                res += num * sigh
                sigh = 1
                num, i = self.getNum(s, i)
            elif op == '-':
                res += num * sigh
                sigh = -1
                num, i = self.getNum(s, i)
            elif op == '*':
                temp, i = self.getNum(s, i)
                num *= temp
            else:
                temp, i = self.getNum(s, i)
                num //= temp
        return res
    
    def getNum(self, s, i):
        while not s[i]:
            i += 1
        pre = i
        while i < len(s) and s[i] not in ('+', '-', '*', '/'):
            i += 1
        return (int(s[pre:i]), i)

s = '1-1'
print(Solution().calculate(s))
