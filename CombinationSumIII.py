class Solution(object):
    def __init__(self):
        self.ans = []
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.combinationSum3Helper(k, n, 1, [])
        return self.ans

    def combinationSum3Helper(self, k, n, start, l):
        if k == 1:
            if n < start or n > 9:
                return
            l += n,
            self.ans += l,
            return
        for i in range(start, min(n//k + 1, 10)):
            t = l[:]
            t += i,
            self.combinationSum3Helper(k-1, n-i, i+1, t)

k, n = 3, 9
print Solution().combinationSum3(k, n)
