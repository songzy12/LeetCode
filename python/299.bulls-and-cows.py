class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        s = [0 for i in range(10)]
        g = [0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                s[int(secret[i])] += 1
                g[int(guess[i])] += 1
        b = 0
        for i in range(10):
            b += min(s[i], g[i])
        return str(a)+'A'+str(b)+'B'

print Solution().getHint('1123','0111')
print Solution().getHint('1807','7810')
