class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = [1 for i in range(n+1)]
        for i in range(1,n+1):
            fact[i] = fact[i-1]*i
        ans = [-1 for i in range(n)]
        v = [False for i in range(n)]
        for i in range(n):
            t = fact[n-1-i]
            q, r = divmod(k, t)
            if r == 0:
                q = q - 1
                r = t
            k = r
            count = j = 0
            while j < n:
                if not v[j]:
                    count += 1
                if count == q+1:
                    break
                j += 1
            ans[i] = j+1
            v[j] = True
        return ''.join([str(i) for i in ans])

for i in range(1, 7):
    print Solution().getPermutation(3, i)
