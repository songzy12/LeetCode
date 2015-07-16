class Solution:
    # @param {integer} n
    # @return {integer}
    '''def countDigitOne(self, n):
        if n < 0:
            return 0
        ans = 0
        n = str(n)
        for i in range(len(n)):
            exp = len(n) - 1 - i
            pre = int(n[:i]) if n[:i] else 0
            mid = int(n[i])
            post = int(n[i+1:]) if n[i+1:] else 0
            ans += pre * 10**exp
            if mid > 1:
                ans += 10**exp
            elif mid == 1:
                ans += post+1
        return ans'''
    def countDigitOne(self, n):
        # (a+8)/10 distinct [0,1] from [2,...,9]
        return sum((n//m+8)//10*m + (n//m%10==1)*(n%m+1) for m in (10**i for i in range(10)))

n = 12345
print(Solution().countDigitOne(n)) # 6

ans = 0
for i in range(n+1):
    ans += str(i).count('1')
print(ans)
